from django.views.generic import TemplateView, CreateView
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from ccam.people.coordinators.forms import CoordinatorsMultiForm
from ccam.people.coordinators.models import Coordinator


# Create your views here.
class CoordinatorsHomeView(TemplateView):
    template_name = "coordinators/home.html"


class CoordinatorsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CoordinatorsMultiForm
    template_name = "coordinators/coordinators_form.html"
    model = Coordinator
    success_url = reverse_lazy("people:managers:home")
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
