from django import forms

from ccam.people.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("registration", "cpf", "profile_picture", "phone_number", "email", "sex")
