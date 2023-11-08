from django.db import models
from django.utils.translation import gettext_lazy as _

from ccam.core.constants import MAX_LENGTH_PHONE_LINE_FIELD
from ccam.core.models import BaseModel
from ccam.people.models import Person


class SEACStaff(BaseModel):
    class Role(models.TextChoices):
        COORDINATOR = "CO", _("Coordenador")
        EMPLOYEE = "FU", _("Funcionário")

    phone_line = models.CharField(max_length=MAX_LENGTH_PHONE_LINE_FIELD, unique=True)
    role = models.CharField(max_length=2, choices=Role.choices)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="person")

    class Meta:
        verbose_name = _("SEAC Staff")
        verbose_name_plural = _("SEAC Staff")

    def __str__(self):
        return f"{self.person.name} - {self.person.registration} - {self.role}"
