from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ccam.people.mixins import UserIsSeacCoordinatorTestMixin


class ManagerHomeView(LoginRequiredMixin, UserIsSeacCoordinatorTestMixin, TemplateView):
    template_name = "managers/home.html"
