from django.views.generic import TemplateView


class StudentHomeView(TemplateView):
    template_name = "students/home.html"


class StudentListView(TemplateView):
    template_name = "students/students_list.html"


class StudentCreateView(TemplateView):
    template_name = "students/students_form.html"


class StudentDetailView(TemplateView):
    template_name = "students/students_detail.html"
