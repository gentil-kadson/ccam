from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

from ccam.core.models import BaseModel
from ccam.people.coordinators.models import Coordinator
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

    accessed_by = models.ForeignKey(SEACStaff, on_delete=models.CASCADE, related_name="knowledge_certificate_assessor")
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE,
                                related_name="knowledge_certificate_student")
    subjects = models.ManyToManyField(
        Subject, related_name="knowledge_certifiace_subjects", through='KnowledgeCGrades')

    class Meta:
        verbose_name = _("Knowledge Certificate")
        verbose_name_plural = _("Knowledge Certificates")

    def __str__(self):
        return f'{self.subjects}, {self.student.person.name} - {self.student.person.registration}'


class KnowledgeCGrades(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="knowledge_certificate_subject")
    knowledge_certificate = models.ForeignKey(
        KnowledgeCertificate, on_delete=models.CASCADE, related_name="specific_knowledge_certificate")
    grade = models.PositiveSmallIntegerField(verbose_name=_("Nota"), validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = _("KnowledgeCGrades")
        verbose_name_plural = _("KnowledgeCGrades")

    def __str__(self):
        return f'{self.subject}; \n{self.knowledge_certificate.student.person.name}; \n{self.knowledge_certificate.student.person.registration}'


class SubjectDispensal(BaseModel):
    class Status(models.TextChoices):
        APPROVED = "AP", _("Aprovado")
        ANALYZING = "PR", _("Em análise")
        REJECTED = "ERR", _("Recusado")

    accessed_by = models.ForeignKey(SEACStaff, on_delete=models.CASCADE, related_name="subject_dispensal_assessor")
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name="subject_dispensal_student")
    subjects = models.ManyToManyField(Subject, related_name="subject_dispensal_subjects", through='SubjectDGrades')

    class Meta:
        verbose_name = _("Subject Dispensal")
        verbose_name_plural = _("Subject Dispensals")

    def __str__(self):
        return f'{self.subjects}, {self.student.person.name} - {self.student.person.registration}'


class SubjectDGrades(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_dispensal_subject")
    subject_dispensal = models.ForeignKey(
        SubjectDispensal, on_delete=models.CASCADE, related_name="specific_subject_dispensal")
    compatibility = models.PositiveSmallIntegerField(verbose_name=_(
        "Compatibilidade"), validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = _("SubjectDGrades")
        verbose_name_plural = _("SubjectDGrades")

    def __str__(self):
        return f'{self.subject}; \n{self.subject_dispensal.student.person.name}; \n{self.subject_dispensal.student.person.registration}'
