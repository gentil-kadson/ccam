from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Person

User = get_user_model()


@receiver(signal=pre_save, sender=Person)
def create_person_auth_user(sender, instance: Person, **kwargs):
    with transaction.atomic():
        if not instance.user:
            auth_user = User.objects.create_user(name=instance.registration, password=instance.cpf)
            instance.user = auth_user
            instance.save()
