from django.shortcuts import render

# Create your views here.
from taverna_dos_pdfs.models import PdfFile


def pdf_list(request):
    pdfs = PdfFile.objects.filter(deleted_at__isnull=False).order_by('votes')
    return render(request, 'taverna_dos_pdfs/pdf_list.html', {'pdfs': pdfs})
