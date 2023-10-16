from django.urls import include, path

app_name = "people"

urlpatterns = [path("students/", include("people.students.urls")), path("seac/", include("people.seac.urls"))]
