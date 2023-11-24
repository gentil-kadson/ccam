from django.urls import path

from ccam.people.coordinators import views

app_name = "coordinators"

urlpatterns = [
    path("", views.CoordinatorsHomeView.as_view(), name="home"),
    path("update/<int:pk>/", views.CoordinatorsUpdateView.as_view(), name="update"),
    path("create/", views.CoordinatorsCreateView.as_view(), name="create"),
    path("list/", views.CoordinatorsListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.CoordinatorsDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", views.CoordinatorsDeleteView.as_view(), name="delete")
]
