from django.contrib import admin
from .models import Course, Subject, KnowledgeCertificate, Committee, KnowledgeCGrades, SubjectDGrades, SubjectDispensal

# Register your models here.
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(KnowledgeCertificate)
admin.site.register(Committee)
admin.site.register(KnowledgeCertificate)
admin.site.register(KnowledgeCGrades)
admin.site.register(SubjectDGrades)
admin.site.register(SubjectDispensal)
