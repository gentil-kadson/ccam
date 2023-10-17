from django.views.generic import TemplateView


# Create your views here.
class CoordinatorsHomeView(TemplateView):
    template_name = "coordinators/home.html"
