from django.views.generic import TemplateView


class SeacHomeView(TemplateView):
    template_name = "seac/home.html"


class SeacStaffListView(TemplateView):
    template_name = "seac/seac_staff_list.html"


class SeacStaffCreateView(TemplateView):
    template_name = "seac/seac_form.html"


class SeacStaffDetailView(TemplateView):
    template_name = "seac/seac_detail.html"
