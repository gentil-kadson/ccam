from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ccam.core.constants import MAX_LENGTH_PHONE_LINE_FIELD
from ccam.people.models import BaseModel, Person


class SEACStaff(BaseModel):
    class Role(models.TextChoices):
        COORDINATOR = "CO", _("Coordenador")
        EMPLOYEE = "FU", _("Funcionário")

    phone_line = models.CharField(max_length=MAX_LENGTH_PHONE_LINE_FIELD, unique=True, verbose_name=_("Fone Ramal"))
    role = models.CharField(max_length=2, choices=Role.choices, verbose_name=_("Responsabilidade"))
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="person")

    class Meta:
        verbose_name = _("Funcionário da SEAC")
        verbose_name_plural = _("Funcionários da SEAC")

    def __str__(self):
        return f"{self.person.name} - {self.person.registration} - {self.role}"

    def get_absolute_url(self):
        return reverse("people:seac:detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("people:seac:update", kwargs={"pk": self.pk})
