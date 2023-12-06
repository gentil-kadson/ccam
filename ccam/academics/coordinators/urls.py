from django.urls import path

from ccam.academics.coordinators import views

urlpatterns = [
    path("subjects/create/", views.SubjectCreateView.as_view(), name="subjects_create"),
    path("subjects/list/", views.SubjectListView.as_view(), name="subjects_list"),
    path("subjects/update/<int:pk>/", views.SubjectUpdateView.as_view(), name="subjects_update"),
    path("subjects/detail/<int:pk>/", views.SubjectDetailView.as_view(), name="subjects_detail"),
    path("subjects/delete/<int:pk>/", views.SubjectDeleteView.as_view(), name="subjects_delete"),
    path("committees/create/", views.CommitteeCreateView.as_view(), name="committees_create"),
    path("committees/list/", views.CommitteeListView.as_view(), name="committees_list"),
]
