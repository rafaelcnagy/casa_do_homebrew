from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from taverna_dos_pdfs.forms import PdfForm
from taverna_dos_pdfs.models import PdfFile


def pdf_list(request):
    pdfs = PdfFile.objects.filter(deleted_at__isnull=True).order_by('votes')
    return render(request, 'taverna_dos_pdfs/pdf_list.html', {'pdfs': pdfs})


@login_required
def create_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        form.author = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PdfForm()
    return render(request, 'taverna_dos_pdfs/create_pdf.html', {'form': form})


def handle_uploaded_file(file):
    with open(f'data/pdfs/test.pdf', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
