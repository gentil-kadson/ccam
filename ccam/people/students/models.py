from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ccam.core.models import BaseModel, GradeSemester
from ccam.people.models import Person


class Student(BaseModel):
    current_grade_semester = models.PositiveSmallIntegerField(
        verbose_name=_("Ano/Período"), choices=GradeSemester.choices
    )
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="student_person")
    course = models.ForeignKey("academics.Course", on_delete=models.CASCADE, related_name="student_course")

    class Meta:
        verbose_name = _("Aluno")
        verbose_name_plural = _("Alunos")

    def __str__(self) -> str:
        return f"{self.person.name} - {self.person.registration} - {self.person.phone_number}"

    def get_absolute_url(self):
        return reverse("people:students:detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("people:students:update", kwargs={"pk": self.pk})
