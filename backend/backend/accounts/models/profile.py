from django.db import models
from django.utils.translation import gettext_lazy as _

from . import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE,
        verbose_name=_("user"),
    )

    def __str__(self):
        return f"{self.user}"
