from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from ccam.people.coordinators.models import Coordinator
from ccam.core.constants import COURSE_COORDINATOR_GROUP_NAME


@receiver(signal=post_save, sender=Coordinator)
def assign_coordinator_group(sender, instance: Coordinator, created, **kwargs):
    if created:
        group = Group.objects.get(name=COURSE_COORDINATOR_GROUP_NAME)
        instance.person.user.groups.add(group)
