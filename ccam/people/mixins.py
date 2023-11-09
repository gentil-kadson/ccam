from ccam.people.forms import PersonForm


class PersonFormMixin:
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["person_form"] = PersonForm()
        return context
