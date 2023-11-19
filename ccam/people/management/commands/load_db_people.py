from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from ccam.core.constants import (
    COURSE_COORDINATOR_GROUP_NAME,
    SEAC_COORDINATOR_GROUP_NAME,
    SEAC_EMPLOYEE_GROUP_NAME,
    STUDENT_GROUP_NAME,
    TEACHER_GROUP_NAME,
)


class Command(BaseCommand):
    help = "Creates all people custom groups for permission management"

    def log_group_creation_feedback(self, group_name, created):
        if created:
            self.stdout.write(self.style.SUCCESS(f"{group_name} group created"))
        else:
            self.stdout.write(self.style.WARNING(f"{group_name} group already created"))

    def handle(self, *args, **kwargs):
        _, coordinator_created = Group.objects.get_or_create(name=COURSE_COORDINATOR_GROUP_NAME)
        _, student_created = Group.objects.get_or_create(name=STUDENT_GROUP_NAME)
        _, seac_coordinator_created = Group.objects.get_or_create(name=SEAC_COORDINATOR_GROUP_NAME)
        _, seac_employee_created = Group.objects.get_or_create(name=SEAC_EMPLOYEE_GROUP_NAME)
        _, teacher_created = Group.objects.get_or_create(name=TEACHER_GROUP_NAME)

        self.log_group_creation_feedback(COURSE_COORDINATOR_GROUP_NAME, coordinator_created)
        self.log_group_creation_feedback(STUDENT_GROUP_NAME, student_created)
        self.log_group_creation_feedback(SEAC_COORDINATOR_GROUP_NAME, seac_coordinator_created)
        self.log_group_creation_feedback(SEAC_EMPLOYEE_GROUP_NAME, seac_employee_created)
        self.log_group_creation_feedback(TEACHER_GROUP_NAME, teacher_created)
