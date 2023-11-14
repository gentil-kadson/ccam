from django import forms

from ccam.people.seac.models import SEACStaff


class SEACStaffForm(forms.ModelForm):
    class Meta:
        model = SEACStaff
        fields = ("phone_line", "role")
