from django import forms

from taverna_dos_pdfs.models import PdfFile


class PdfForm(forms.ModelForm):
    class Meta:
        model = PdfFile
        fields = ('title', 'description', 'pdf')
