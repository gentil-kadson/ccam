from django.urls import path

from ccam.people.directors import views

app_name = "directors"

urlpatterns = [path("list/", views.DirectorListView.as_view(), name="list")]
