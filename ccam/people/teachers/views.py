from django.views.generic import TemplateView


class TeacherListView(TemplateView):
    template_name = "teachers/teachers_list.html"


class TeacherCreateView(TemplateView):
    template_name = "teachers/teachers_form.html"
