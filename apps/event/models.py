from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    users = models.ManyToManyField(User, verbose_name=_("Users"), blank=True)
    description = models.TextField(_("Description"), blank=True)
    location = models.CharField(_("Location"), max_length=100)
    start_time = models.DateTimeField(_("Start time"))
    end_time = models.DateTimeField(_("End time"))

    def __str__(self):
        return self.name
