from django.db import models
from django.utils.translation import gettext_lazy as _

from ccam.core.models import BaseModel
from ccam.people.models import Person


class Coordinator(BaseModel):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="coordinator_person")

    class Meta:
        verbose_name = _("Coordinator")
        verbose_name_plural = _("Coordinators")

    def __str__(self):
        return f'{self.person.name} - {self.person.registration}'
