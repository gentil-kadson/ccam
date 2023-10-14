from django.views.generic import TemplateView


class StudentHome(TemplateView):
    template_name = "students/home.html"
