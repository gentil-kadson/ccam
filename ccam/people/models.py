import cpf_field.models as cpf_field_models
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from ccam.core.constants import MAX_LENGTH_NAME_FIELD, MAX_LENGTH_PHONE_NUMBER_FIELD, MAX_LENGTH_REGISTRATION_FIELD, MAX_LENGTH_PHONE_LINE_FIELD
from ccam.core.models import BaseModel
from ccam.core.utils import user_directory_path


class Person(BaseModel):
    class Sex(models.TextChoices):
        MALE = "M", _("Masculino")
        FEMALE = "F", _("Feminino")

    name = models.CharField(max_length=MAX_LENGTH_NAME_FIELD, verbose_name=_("Nome"))
    profile_picture = models.ImageField(verbose_name=_("Foto de perfil"), upload_to=user_directory_path)
    email = models.EmailField(unique=True, verbose_name=_("E-mail"))
    registration = models.CharField(max_length=MAX_LENGTH_REGISTRATION_FIELD, unique=True, verbose_name=_("Matrícula"))
    sex = models.CharField(max_length=1, choices=Sex.choices, verbose_name=_("Sexo"))
    cpf = cpf_field_models.CPFField(verbose_name=_("CPF"), unique=True)
    phone_number = models.CharField(verbose_name=_("Fone"), max_length=MAX_LENGTH_PHONE_NUMBER_FIELD)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="person")

    class Meta:
        verbose_name = _("Pessoa")
        verbose_name_plural = _("Pessoas")

    def __str__(self):
        return f"{self.name} - {self.registration}"
