from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from ccam.core.constants import TEACHER_GROUP_NAME
from ccam.people.teachers.models import Teacher


@receiver(signal=post_save, sender=Teacher)
def assign_teacher_group(sender, instance: Teacher, created, **kwargs):
    if created:
        group = Group.objects.get(name=TEACHER_GROUP_NAME)
        instance.person.user.groups.add(group)
