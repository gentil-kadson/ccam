from django.views.generic import TemplateView


class DirectorListView(TemplateView):
    template_name = "directors/directors_list.html"


class DirectorCreateView(TemplateView):
    template_name = "directors/directors_form.html"


class DirectorDetailView(TemplateView):
    template_name = "directors/directors_detail.html"
