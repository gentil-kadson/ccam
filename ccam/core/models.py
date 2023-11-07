from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def get_sentinel_user():
    return User.objects.get_or_create(username="deleted")[0]


class TimeStampedModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    changed_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel):
    created_by = models.ForeignKey(
        to=User, on_delete=models.SET(get_sentinel_user().id), related_name="%(app_label)s_%(class)s_created_by"
    )
    updated_by = models.ForeignKey(
        to=User, on_delete=models.SET(get_sentinel_user().id), related_name="%(app_label)s_%(class)s_updated_by"
    )

    class Meta:
        abstract = True
