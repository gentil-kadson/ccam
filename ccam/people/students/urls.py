from django.urls import path

from ccam.people.students import views

app_name = "students"

urlpatterns = [
    path("", views.StudentHomeView.as_view(), name="home"),
    path("list/", views.StudentListView.as_view(), name="list"),
    path("create/", views.StudentCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", views.StudentDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", views.StudentDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", views.StudentUpdateView.as_view(), name="update"),
]
