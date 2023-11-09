from django.views.generic import CreateView, TemplateView

from ccam.people.mixins import PersonFormMixin

from .forms import SEACStaffForm


class SeacHomeView(TemplateView):
    template_name = "seac/home.html"


class SeacStaffListView(TemplateView):
    template_name = "seac/seac_staff_list.html"


class SeacStaffCreateView(PersonFormMixin, CreateView):
    form_class = SEACStaffForm
    template_name = "seac/seac_staff_form.html"


class SeacStaffDetailView(TemplateView):
    template_name = "seac/seac_detail.html"
