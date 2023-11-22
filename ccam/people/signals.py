from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver

from ccam.people.utils import clean_cpf

from .models import Person

User = get_user_model()


@receiver(signal=pre_save, sender=Person)
def create_person_auth_user(sender, instance: Person, **kwargs):
    with transaction.atomic():
        cleaned_cpf = clean_cpf(instance.cpf)
        try:
            auth_user = User.objects.get(username=instance.registration)
            auth_user.username = instance.registration
            auth_user.password = cleaned_cpf
            auth_user.save()
        except User.DoesNotExist:
            auth_user = User.objects.create_user(username=instance.registration, password=cleaned_cpf)
            instance.user = auth_user
