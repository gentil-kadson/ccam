from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

from ccam.core.models import BaseModel
from ccam.people.models import Person


class Student(BaseModel):
    current_grade_semester = models.PositiveSmallIntegerField(
        verbose_name=_("Ano/Período"), validators=[MaxValueValidator(8)])
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="person")

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self) -> str:
        return f'{self.person.name} - {self.person.registration} - {self.person.phone_number}'
