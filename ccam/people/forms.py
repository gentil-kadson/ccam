from django import forms

from ccam.core.widgets import CCAMFileWidget
from ccam.people.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name", "registration", "cpf", "profile_picture", "phone_number", "email", "sex")
        widgets = {"profile_picture": CCAMFileWidget(attrs={"label": "Foto de perfil"})}
