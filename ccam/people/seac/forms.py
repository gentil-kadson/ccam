from betterforms.multiform import MultiModelForm
from django import forms

from ccam.people.forms import PersonForm
from ccam.people.seac.models import SEACStaff


class SEACStaffForm(forms.ModelForm):
    class Meta:
        model = SEACStaff
        fields = ("phone_line", "role")


class SEACStaffPersonMultiForm(MultiModelForm):
    form_classes = {"person": PersonForm, "seacstaff": SEACStaffForm}
