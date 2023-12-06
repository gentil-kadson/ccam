from django.contrib.auth.mixins import UserPassesTestMixin

from ccam.core.constants import SEAC_COORDINATOR_GROUP_NAME, STUDENT_GROUP_NAME


class UserIsStudentTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name=STUDENT_GROUP_NAME).exists()


class UserIsSeacCoordinatorTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name=SEAC_COORDINATOR_GROUP_NAME).exists()
