from django.contrib import messages


class SuccessMessageMixin:
    success_message = None

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        print("----------------- FUI CHAMADO ------------------------")
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return form_valid
