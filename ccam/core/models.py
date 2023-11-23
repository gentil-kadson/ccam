from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class TimeStampedModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    changed_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel):
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name="%(app_label)s_%(class)s_created_by",
    )
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
        related_name="%(app_label)s_%(class)s_updated_by",
    )

    class Meta:
        abstract = True


class EducationalLevel(models.TextChoices):
    TECHNICIAN = "TEEM", _("Técnico Médio Integrado")
    UNIVERSITY = "UNI", _("Superior")
