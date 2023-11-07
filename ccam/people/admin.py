from django.contrib import admin

from .models import Person
from .seac.models import SEACStaff

admin.site.register(SEACStaff)
admin.site.register(Person)
