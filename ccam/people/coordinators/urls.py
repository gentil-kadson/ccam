from django.urls import path

from ccam.people.coordinators import views

app_name = "coordinators"

urlpatterns = [
    path("", views.CoordinatorsHomeView.as_view(), name="home"),
    path("create/", views.CoordinatorsCreateView.as_view(), name="create"),
    path("list/", views.CoordinatorsListView.as_view(), name="list")
]
