from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView

from taverna_dos_pdfs.forms import PdfForm
from taverna_dos_pdfs.models import PdfFile


class PdfList(ListView):
    model = PdfFile


class PdfDetail(DetailView):
    model = PdfFile
    fields = ('title', 'description', 'pdf')


class PdfUpdate(UpdateView):
    model = PdfFile
    fields = ('title', 'description', 'pdf')



class PdfDelete(DeleteView):
    model = PdfFile
    success_url = reverse_lazy('pdf_list')


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
    return render(request, 'taverna_dos_pdfs/pdf_create.html', {'form': form})

