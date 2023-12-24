from django.db import models
from django.urls import reverse
from django.utils.text import get_text_list
from django.utils.translation import gettext_lazy as _

from ccam.academics.models import Subject
from ccam.core.models import BaseModel
from ccam.people.models import Person


class Teacher(BaseModel):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="teacher_person")
    subjects = models.ManyToManyField(Subject, related_name="teacher_subjects", verbose_name=_("Matérias"))

    class Meta:
        verbose_name = _("Professor")
        verbose_name_plural = _("Professores")

    def __str__(self):
        return f"{self.person.name} - {self.person.registration}"

    def get_absolute_url(self):
        return reverse("people:teachers:detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("people:teachers:update", kwargs={"pk": self.pk})

    def get_subjects_names(self):
        teacher_subjects = list(self.subjects.values_list("name", flat=True))
        teacher_subjects = get_text_list(teacher_subjects, "e")
        return teacher_subjects
