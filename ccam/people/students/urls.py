from django.urls import path

from ccam.people.students import views

app_name = "students"

urlpatterns = [
    path("", views.StudentHomeView.as_view(), name="home"),
    path("list/", views.StudentListView.as_view(), name="list"),
]
