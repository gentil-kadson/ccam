from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from ccam.core.models import BaseModel, EducationalLevel


class Course(BaseModel):
    name = models.CharField(max_length=280, verbose_name=_("Nome do curso"))
    duration = models.SmallIntegerField(
        verbose_name=_("Duração (em anos/períodos)"), validators=[MaxValueValidator(8)]
    )
    coordinator = models.OneToOneField(
        "coordinators.Coordinator", on_delete=models.CASCADE, related_name="course", null=True
    )

    class Meta:
        verbose_name = _("Curso")
        verbose_name_plural = _("Cursos")

    def __str__(self) -> str:
        return f"{self.name}"


class Subject(BaseModel):
    name = models.CharField(max_length=40, verbose_name=_("Disciplina"))
    course = models.ManyToManyField(Course, related_name="subjects")
    grade_semester_availability = models.PositiveSmallIntegerField(
        verbose_name=_("Ano/Período"), validators=[MaxValueValidator(8)], default=1
    )
    educational_level = models.CharField(
        max_length=4, choices=EducationalLevel.choices, verbose_name=_("Nível Educacional")
    )

    class Meta:
        verbose_name = _("Disciplina")
        verbose_name_plural = _("Disciplinas")

    def __str__(self):
        return f"{self.name} - {self.get_educational_level_display()}"


class KnowledgeCertificate(BaseModel):
    class Status(models.TextChoices):
        APPROVED = "AP", _("Aprovado")
        ANALYZING = "PR", _("Em análise")
        REJECTED = "ERR", _("Recusado")

    assessed_by = models.ForeignKey(
        "seac.SEACStaff", on_delete=models.CASCADE, related_name="knowledge_certificate_assessor"
    )
    student = models.ForeignKey(
        "students.Student", on_delete=models.CASCADE, related_name="knowledge_certificate_student"
    )
    subjects = models.ManyToManyField(
        Subject, related_name="knowledge_certifiace_subjects", through="KnowledgeCGrades"
    )

    class Meta:
        verbose_name = _("Certificação de Conhecimento")
        verbose_name_plural = _("Certificação de Conhecimentos")

    def __str__(self):
        return f"{self.subjects}, {self.student.person.name} - {self.student.person.registration}"


class KnowledgeCGrades(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="knowledge_certificate_subject")
    knowledge_certificate = models.ForeignKey(
        KnowledgeCertificate, on_delete=models.CASCADE, related_name="specific_knowledge_certificate"
    )
    grade = models.PositiveSmallIntegerField(verbose_name=_("Nota"), validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = _("CertificaçãoCNotas")
        verbose_name_plural = _("CertificaçãoCNotas")

    def __str__(self):
        return (
            f"{self.subject};"
            f"\n{self.knowledge_certificate.student.person.name};"
            f"\n{self.knowledge_certificate.student.person.registration}"
        )


class SubjectDispensal(BaseModel):
    class Status(models.TextChoices):
        APPROVED = "AP", _("Aprovado")
        ANALYZING = "PR", _("Em análise")
        REJECTED = "ERR", _("Recusado")

    assessed_by = models.ForeignKey(
        "seac.SEACStaff", on_delete=models.CASCADE, related_name="subject_dispensal_assessor"
    )
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name="subject_dispensal_student")
    subjects = models.ManyToManyField(Subject, related_name="subject_dispensal_subjects", through="SubjectDGrades")

    class Meta:
        verbose_name = _("Aproveitamento de Disciplina")
        verbose_name_plural = _("Aproveitamento de Disciplinas")

    def __str__(self):
        return f"{self.subjects}, {self.student.person.name} - {self.student.person.registration}"


class SubjectDGrades(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_dispensal_subject")
    subject_dispensal = models.ForeignKey(
        SubjectDispensal, on_delete=models.CASCADE, related_name="specific_subject_dispensal"
    )
    compatibility = models.PositiveSmallIntegerField(
        verbose_name=_("Compatibilidade"), validators=[MaxValueValidator(100)]
    )

    class Meta:
        verbose_name = _("AproveitamentoDCompatibilidades")
        verbose_name_plural = _("AproveitamentoDCompatibilidades")

    def __str__(self):
        return (
            f"{self.subject};"
            f"\n{self.subject_dispensal.student.person.name};"
            f"\n{self.subject_dispensal.student.person.registration}"
        )


class Committee(BaseModel):
    coordinator = models.ForeignKey(
        "coordinators.Coordinator", on_delete=models.CASCADE, related_name="committee_coordinator"
    )
    teachers = models.ManyToManyField("teachers.Teacher", related_name="committee_teachers")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="committee_subject")

    class Meta:
        verbose_name = _("Banca")
        verbose_name_plural = _("Bancas")

    def __str__(self):
        return f"{self.subject.name}"
