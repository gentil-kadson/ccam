from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SEACStaffForm
from .models import SEACStaff


class SeacHomeView(TemplateView):
    template_name = "seac/home.html"


class SeacStaffListView(TemplateView):
    template_name = "seac/seac_staff_list.html"


class SeacStaffCreateView(LoginRequiredMixin, CreateView):
    form_class = SEACStaffForm
    template_name = "seac/seac_staff_form.html"
    model = SEACStaff
    success_url = reverse_lazy("people:managers:home")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class SeacStaffDetailView(TemplateView):
    template_name = "seac/seac_detail.html"
