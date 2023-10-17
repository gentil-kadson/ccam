from django.urls import path

from ccam.people.managers import views

app_name = "managers"

urlpatterns = [path("", views.ManagerHomeView.as_view(), name="home")]
