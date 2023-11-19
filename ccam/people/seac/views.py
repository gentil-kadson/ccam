from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, TemplateView
from django_filters.views import FilterView

from .filters import SEACStaffFilterSet
from .forms import SEACStaffPersonMultiForm
from .models import SEACStaff


class SeacHomeView(TemplateView):
    template_name = "seac/home.html"


class SeacStaffListView(LoginRequiredMixin, FilterView):
    model = SEACStaff
    filterset_class = SEACStaffFilterSet
    template_name = "seac/seac_staff_filter.html"
    paginate_by = settings.PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_page = int(self.request.GET.get("page", 1))
        context.update({"current_page": current_page})
        return context


class SeacStaffCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = SEACStaffPersonMultiForm
    template_name = "seac/seac_staff_form.html"
    model = SEACStaff
    success_url = reverse_lazy("people:managers:home")
    success_message = _("Funcionário da SEAC criado com sucesso!")

    @transaction.atomic
    def form_valid(self, form):
        person = form["person"].save(commit=False)
        person.created_by = self.request.user
        person.updated_by = self.request.user
        seac_staff = form["seacstaff"].save(commit=False)
        seac_staff.person = person
        seac_staff.created_by = self.request.user
        seac_staff.updated_by = self.request.user
        return super().form_valid(form)


class SeacStaffDetailView(TemplateView):
    template_name = "seac/seac_detail.html"
