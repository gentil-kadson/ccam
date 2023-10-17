from django.views.generic import TemplateView


class DirectorListView(TemplateView):
    template_name = "directors/directors_list.html"
