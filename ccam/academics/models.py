from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

from ccam.core.models import BaseModel
from ccam.people.coordinators.models import Coordinator


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
