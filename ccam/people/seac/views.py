from django.views.generic import TemplateView


class SeacHomeView(TemplateView):
    template_name = "seac/home.html"
