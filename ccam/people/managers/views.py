from django.views.generic import TemplateView


class ManagerHomeView(TemplateView):
    template_name = "managers/home.html"
