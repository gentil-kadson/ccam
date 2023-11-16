from django.contrib import admin

from ccam.people.models import Person
from ccam.people.coordinators.models import Coordinator
from ccam.people.seac.models import SEACStaff
from ccam.people.students.models import Student
from ccam.people.teachers.models import Teacher

admin.site.register(SEACStaff)
admin.site.register(Person)
admin.site.register(Coordinator)
admin.site.register(Student)
admin.site.register(Teacher)
