from django.contrib.auth.mixins import UserPassesTestMixin

from ccam.core.constants import (
    COURSE_COORDINATOR_GROUP_NAME,
    SEAC_COORDINATOR_GROUP_NAME,
    SEAC_EMPLOYEE_GROUP_NAME,
    STUDENT_GROUP_NAME,
    TEACHER_GROUP_NAME,
)


class PeoplePassesTestBaseMixin(UserPassesTestMixin):
    group_name = ""

    def test_func(self):
        return self.request.user.groups.filter(name=self.group_name).exists()


class UserIsStudentTestMixin(PeoplePassesTestBaseMixin):
    group_name = STUDENT_GROUP_NAME


class UserIsSeacCoordinatorTestMixin(PeoplePassesTestBaseMixin):
    group_name = SEAC_COORDINATOR_GROUP_NAME


class UserIsSeacEmployeeTestMixin(PeoplePassesTestBaseMixin):
    group_name = SEAC_EMPLOYEE_GROUP_NAME


class UserIsCourseCoordinatorTestMixin(PeoplePassesTestBaseMixin):
    group_name = COURSE_COORDINATOR_GROUP_NAME


class UserIsTeacherTestMixin(PeoplePassesTestBaseMixin):
    group_name = TEACHER_GROUP_NAME
