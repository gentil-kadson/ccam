from django.urls import path

from ccam.people.teachers import views

app_name = "teachers"

urlpatterns = [
    path("", views.TeacherHomeView.as_view(), name="home"),
    path("list/", views.TeacherListView.as_view(), name="list"),
    path("create/", views.TeacherCreateView.as_view(), name="create"),
    path("detail/", views.TeacherDetailView.as_view(), name="detail"),
]
