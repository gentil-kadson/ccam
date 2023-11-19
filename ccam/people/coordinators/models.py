from django.db import models
from ccam.people.models import Person
from ccam.academics.models import Course
from ccam.core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Coordinator(BaseModel):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="coordinator_person")

    class Meta:
        verbose_name = _("Coordenador")
        verbose_name_plural = _("Coordenadores")

    def __str__(self):
        return f'{self.person.name} - {self.person.registration}'
