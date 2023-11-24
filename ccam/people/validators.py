import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_number_validator(phone_number: str):
    valid_phone_number = re.match(r"\(\d{2}\) \d{5}-\d{4}", phone_number)
    if not valid_phone_number:
        raise ValidationError(_("Formato de número inválido. Ele dever ser (XX) XXXXX-XXXX"))


def registration_validator(registration: str):
    valid_registration = re.match(r"\d{14}", registration)
    if not valid_registration:
        raise ValidationError(_("A matrícula deve conter somente números"))


def validate_cpf_mask(cpf: str):
    valid_cpf_mask = re.match(r"\d{3}\.\d{3}\.\d{3}\-\d{2}", cpf)
    if not valid_cpf_mask:
        raise ValidationError(_("O CPF deve seguir o formato XXX.XXX.XXX-XX"))
