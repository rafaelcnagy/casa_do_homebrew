from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView

from taverna_dos_pdfs.forms import PdfForm
from taverna_dos_pdfs.models import PdfFile


class PdfList(ListView):
    model = PdfFile


class PdfDetail(DetailView):
    model = PdfFile
    fields = ('title', 'description', 'pdf')


class PdfUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PdfFile
    fields = ('title', 'description', 'pdf')

    def get(self, request, **kwargs):
        if self.get_object().author == self.request.user:
            return UpdateView.get(self, request, **kwargs)
        else:
            messages.add_message(request, messages.WARNING, "Você pode editar apenas seus próprios arquivos")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PdfDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PdfFile
    success_url = reverse_lazy('pdf_list')

    def get(self, request, **kwargs):
        if self.get_object().author == self.request.user:
            return UpdateView.get(self, request, **kwargs)
        else:
            messages.add_message(request, messages.WARNING, "Você pode deletar apenas seus próprios arquivos")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def create_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        form.author = request.user
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PdfForm()
    return render(request, 'taverna_dos_pdfs/pdf_create.html', {'form': form})

