from django.urls import path

from ccam.people.students import views

app_name = "students"

urlpatterns = [path("", views.StudentHome.as_view(), name="home")]
