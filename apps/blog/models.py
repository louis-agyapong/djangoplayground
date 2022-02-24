from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_("title"), blank=True)
    body = models.TextField(_("body"))
    liked = models.ManyToManyField(User, verbose_name=_("liked"), related_name="liked_posts", blank=True)
    created = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    @property
    def comments(self):
        return self.post.all()

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ["-created"]


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=_("post"), on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    body = models.CharField(_("body"), max_length=255)
    created = models.DateTimeField(_("created"), auto_now_add=True)
