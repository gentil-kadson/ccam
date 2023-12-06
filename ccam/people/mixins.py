from django.contrib.auth.mixins import UserPassesTestMixin

from ccam.core.constants import (
    COURSE_COORDINATOR_GROUP_NAME,
    SEAC_COORDINATOR_GROUP_NAME,
    SEAC_EMPLOYEE_GROUP_NAME,
    STUDENT_GROUP_NAME,
    TEACHER_GROUP_NAME,
)


class UserIsStudentTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name=STUDENT_GROUP_NAME).exists()


class UserIsSeacCoordinatorTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name=SEAC_COORDINATOR_GROUP_NAME).exists()


class UserIsSeacEmployeeTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name=SEAC_EMPLOYEE_GROUP_NAME).exists()


class UserIsCourseCoordinatorTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name=COURSE_COORDINATOR_GROUP_NAME).exists()


class UserIsTeacherTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name=TEACHER_GROUP_NAME).exists()
