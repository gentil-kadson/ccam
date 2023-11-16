from django.db import models
from django.core.validators import MaxValueValidator
from ccam.people.models import Person
from ccam.core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Student(BaseModel):
    current_grade_semester = models.PositiveSmallIntegerField(
        verbose_name=_("Ano/Período"), validators=[MaxValueValidator(8)])
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="student_person")
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE, related_name="student_course")

    class Meta:
        verbose_name = _("Aluno")
        verbose_name_plural = _("Alunos")

    def __str__(self) -> str:
        return f'{self.person.name} - {self.person.registration} - {self.person.phone_number}'
