from django.urls import path

from ccam.people.students import views

app_name = "students"

urlpatterns = [
    path("", views.StudentHomeView.as_view(), name="home"),
    path("list/", views.StudentListView.as_view(), name="list"),
    path("create/", views.StudentCreateView.as_view(), name="create"),
    path("detail/<pk>/", views.StudentDetailView.as_view(), name="detail"),
    path("delete/", views.StudentDeleteView.as_view(), name="delete"),
    path("update/<pk>/", views.StudentUpdateView.as_view(), name="update")
]
