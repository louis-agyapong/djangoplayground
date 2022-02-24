from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
