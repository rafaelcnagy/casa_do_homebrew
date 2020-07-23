from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from taverna_dos_pdfs.models import PdfFile


class PdfForm(forms.ModelForm):
    class Meta:
        model = PdfFile
        fields = ('title', 'description', 'pdf')


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Nome')
    last_name = forms.CharField(max_length=60, label='Sobrenome')
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
