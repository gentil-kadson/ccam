from django.urls import path

from ccam.people.teachers import views

app_name = "teachers"

urlpatterns = [
    path("list/", views.TeacherListView.as_view(), name="list"),
    path("create/", views.TeacherCreateView.as_view(), name="create"),
]
