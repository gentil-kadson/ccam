from django.urls import path

from ccam.people.seac import views

app_name = "seac"

urlpatterns = [
    path("", views.SeacHomeView.as_view(), name="home"),
    path("list/", views.SeacStaffListView.as_view(), name="list"),
    path("create/", views.SeacStaffCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", views.SeacStaffDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", views.SeacStaffUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.SeacStaffDeleteView.as_view(), name="delete"),
]
