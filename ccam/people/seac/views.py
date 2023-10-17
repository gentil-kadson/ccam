from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class SeacHomeView(TemplateView):
    template_name = "seac/home.html"
