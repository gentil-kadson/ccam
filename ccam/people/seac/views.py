from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SEACStaffPersonMultiForm
from .models import SEACStaff


class SeacHomeView(TemplateView):
    template_name = "seac/home.html"


class SeacStaffListView(TemplateView):
    template_name = "seac/seac_staff_list.html"


class SeacStaffCreateView(LoginRequiredMixin, CreateView):
    form_class = SEACStaffPersonMultiForm
    template_name = "seac/seac_staff_form.html"
    model = SEACStaff
    success_url = reverse_lazy("people:managers:home")

    def form_valid(self, form):
        person = form["person"].save(commit=False)
        person.created_by = self.request.user
        person.updated_by = self.request.user
        person.save()
        seac_staff = form["seacstaff"].save(commit=False)
        seac_staff.person = person
        seac_staff.created_by = self.request.user
        seac_staff.updated_by = self.request.user
        seac_staff.save()
        return redirect(self.success_url)


class SeacStaffDetailView(TemplateView):
    template_name = "seac/seac_detail.html"
