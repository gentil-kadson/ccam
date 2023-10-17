from django.urls import include, path

app_name = "people"

urlpatterns = [
    path("students/", include("people.students.urls")),
    path("seac/", include("people.seac.urls")),
    path("managers/", include("people.managers.urls")),
    path("teachers/", include("people.teachers.urls")),
    path("directors/", include("people.directors.urls")),
]
