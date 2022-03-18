import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ["-pub_date"]
        app_label = "polls"


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices", verbose_name=_("question")
    )
    choice_text = models.CharField(_("Choice text"), max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")
        ordering = ["-votes"]
        app_label = "polls"
