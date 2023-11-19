from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from ccam.people.students.models import Student
from ccam.core.constants import STUDENT_GROUP_NAME


@receiver(signal=post_save, sender=Student)
def assign_student_group(sender, instance: Student, created, **kwargs):
    if created:
        group = Group.objects.get(name=STUDENT_GROUP_NAME)
        instance.person.user.groups.add(group)
