from django.views.generic import TemplateView


class TeacherHomeView(TemplateView):
    template_name = "teachers/home.html"


class TeacherListView(TemplateView):
    template_name = "teachers/teachers_list.html"


class TeacherCreateView(TemplateView):
    template_name = "teachers/teachers_form.html"


class TeacherDetailView(TemplateView):
    template_name = "teachers/teachers_detail.html"
