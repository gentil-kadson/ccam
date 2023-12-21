from django.urls import path

from ccam.academics.coordinators.urls import urlpatterns as coordinators_urls
from ccam.academics.seac.urls import urlpatterns as seac_urls
from ccam.academics.students.urls import urlpatterns as students_urls
from ccam.academics.teachers.urls import urlpatterns as teachers_urls
from ccam.academics.views import CourseSubjects

app_name = "academics"

urlpatterns = [path("course-subjects/", CourseSubjects.as_view(), name="course_subjects")]

urlpatterns += seac_urls
urlpatterns += coordinators_urls
urlpatterns += students_urls
urlpatterns += teachers_urls
