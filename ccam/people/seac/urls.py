from django.urls import path

from ccam.people.seac import views

app_name = "seac"

urlpatterns = [
    path("", views.SeacHomeView.as_view(), name="home"),
    path("list/", views.SeacStaffListView.as_view(), name="list"),
]
