from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from ccam.core.constants import SEAC_COORDINATOR_GROUP_NAME, SEAC_EMPLOYEE_GROUP_NAME
from ccam.people.seac.models import SEACStaff


@receiver(signal=post_save, sender=SEACStaff)
def assign_seac_staff_group(sender, instance: SEACStaff, created, **kwargs):
    if created:
        if instance.role == SEACStaff.Role.COORDINATOR:
            group = Group.objects.get(name=SEAC_COORDINATOR_GROUP_NAME)
        else:
            group = Group.objects.get(name=SEAC_EMPLOYEE_GROUP_NAME)
        instance.person.user.groups.add(group)
