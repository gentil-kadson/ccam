from django import forms

from .models import SEACStaff


class SEACStaffForm(forms.ModelForm):
    class Meta:
        model = SEACStaff
        fields = ("phone_line", "role")
