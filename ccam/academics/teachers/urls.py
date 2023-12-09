from django.urls import path

from ccam.academics.teachers import views

urlpatterns = [
    path("teachers/<int:pk>/committees/", views.TeacherCommitteesListView.as_view(), name="teacher_committees")
]
