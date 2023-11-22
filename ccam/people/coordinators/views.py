from typing import Any

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView

from ccam.core.views import FilteredListView
from ccam.people.coordinators.forms import CoordinatorsMultiForm
from ccam.people.coordinators.models import Coordinator

from .filters import CoordinatorsFilterSet

# Create your views here.


class CoordinatorsHomeView(TemplateView):
    template_name = "coordinators/home.html"


class CoordinatorsDetailView(DetailView):
    model = Coordinator
    template_name = "coordinators/coordinators_detail.html"
    context_object_name = "coordinator"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)


class CoordinatorsListView(LoginRequiredMixin, FilteredListView):
    model = Coordinator
    filterset_class = CoordinatorsFilterSet
    template_name = "coordinators/coordinators_list.html"
    paginate_by = settings.PAGINATE_BY


class CoordinatorsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CoordinatorsMultiForm
    template_name = "coordinators/coordinators_form.html"
    model = Coordinator
    success_url = reverse_lazy("people:coordinators:list")
    success_message = _("Coordenador de curso criado com sucesso!")

    @transaction.atomic
    def form_valid(self, form):
        person = form["person"].save(commit=False)
        person.created_by = self.request.user
        person.updated_by = self.request.user
        coordinator = form["coordinator"].save(commit=False)
        coordinator.person = person
        coordinator.created_by = self.request.user
        coordinator.updated_by = self.request.user
        return super().form_valid(form)


class CoordinatorsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Coordinator
    form_class = CoordinatorsMultiForm
    template_name = "coordinators/coordinators_form.html"
    success_url = reverse_lazy("people:coordinators:list")
    success_message = _("Coordenador de curso editado com sucesso!")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(instance={"person": self.object.person, "coordinator": self.object})
        return kwargs
