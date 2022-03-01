from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        draft = "draft", _("Draft")
        published = "published", _("Published")

    title = models.CharField(max_length=200, verbose_name=_("title"), blank=True)
    slug = models.SlugField(_("slug"), max_length=255, unique_for_date="publish")
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField(_("body"))
    photo = models.ImageField(_("photo"), upload_to="blogs", blank=True, null=True)
    liked = models.ManyToManyField(User, verbose_name=_("liked"), related_name="liked_posts", blank=True)
    publish = models.DateTimeField(_("publish"), default=timezone.now)
    created = models.DateTimeField(_("created at"), auto_now_add=True)
    updated = models.DateTimeField(_("updated at"), auto_now=True)
    status = models.CharField(_(""), max_length=9, choices=StatusChoices.choices, default=StatusChoices.draft)

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )

    def __str__(self):
        return f"{self.title} by {self.author}"

    @property
    def comments(self):
        return self.comments.all()

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ["-publish"]


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=_("post"), on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    body = models.CharField(_("body"), max_length=255)
    created = models.DateTimeField(_("created"), auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s comment on {self.post}"
