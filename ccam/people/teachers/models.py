from django.db import models
from django.utils.translation import gettext_lazy as _

from ccam.core.models import BaseModel
from ccam.people.models import Person
from ccam.academics.models import Subject
# Create your models here.


class Teacher(BaseModel):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="teacher_person")
    subjects = models.ManyToManyField(Subject, related_name="teacher_subjects")

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def __str__(self):
        return f'{self.person.name} - {self.person.registration}'
