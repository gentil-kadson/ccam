from django.views.generic import TemplateView


class ModalView(TemplateView):
    template_name = "core/_confirmation_modal.html"
