from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from taverna_dos_pdfs.forms import PdfForm
from taverna_dos_pdfs.models import PdfFile


def pdf_list(request):
    pdfs = PdfFile.objects.filter(deleted_at__isnull=True).order_by('votes')
    return render(request, 'taverna_dos_pdfs/pdf_list.html', {'pdfs': pdfs})


def create_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PdfForm()
    return render(request, 'taverna_dos_pdfs/create_pdf.html', {'form': form})


def handle_uploaded_file(f):
    with open(f'data/pdfs/test.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
