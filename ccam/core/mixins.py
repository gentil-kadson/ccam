from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect


class UniqueConstraintErrorMessageMixin:
    unique_constraint_error_msg = ""

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as error:
            error_msg = error.args[0]
            is_unique_constraint_error = True if "unique constraint" in error_msg else False
            if is_unique_constraint_error:
                messages.add_message(self.request, level=messages.WARNING, message=self.unique_constraint_error_msg)
                return redirect(self.request.path_info)
            else:
                raise  # Propagates de exception
