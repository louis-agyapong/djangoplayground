from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    name = models.CharField(_("name"), max_length=100)

    def __str__(self) -> str:
        return self.name


class Framework(models.Model):
    name = models.CharField(_("name"), max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="frameworks")

    def __str__(self) -> str:
        return self.name
