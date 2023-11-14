from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

from ccam.core.models import BaseModel
from ccam.people.coordinators.models import Coordinator
from ccam.people.students.models import Student
from ccam.people.seac.models import SEACStaff


class Course(BaseModel):
    name = models.CharField(max_length=40, verbose_name=_("Nome do curso"))
    duration = models.SmallIntegerField(verbose_name=_(
        "Duração (em anos/períodos)"), validators=[MaxValueValidator(8)])
    coordinator = models.OneToOneField(Coordinator, on_delete=models.CASCADE, related_name="coordinator")

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self) -> str:
        return f'{self.name}'


class Subject(BaseModel):
    name = models.CharField(max_length=40, verbose_name=_("Disciplina"))
    course = models.ManyToManyField(Course, related_name="subject_courses")

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return f'{self.name}'


class KnowledgeCertificate(BaseModel):
    class Status(models.TextChoices):
        APPROVED = "AP", _("Aprovado")
        ANALYZING = "PR", _("Em análise")
        REJECTED = "ERR", _("Recusado")

    accessed_by = models.ForeignKey(SEACStaff, on_delete=models.CASCADE, related_name="knowledge_certifiacte_assessor")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="knowledge_certificate_student")
    subjects = models.ManyToManyField(Subject, related_name="knowledge_certifiace_subjects")
