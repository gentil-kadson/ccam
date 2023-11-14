from django.contrib import admin

from .models import Person
from .coordinators.models import Coordinator
# from .students.models import Student
from .seac.models import SEACStaff

admin.site.register(SEACStaff)
admin.site.register(Person)
admin.site.register(Coordinator)
# admin.site.register(Student)
