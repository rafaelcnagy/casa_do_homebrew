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
    queryset = PdfFile.objects.filter(deleted_at__isnull=True).order_by('created_at').order_by('-vote_score')


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

    def get_success_url(self):
        return reverse_lazy('pdf_view', kwargs={'pk': self.kwargs['pk']})


class PdfDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PdfFile
    success_url = reverse_lazy('pdf_list')

    def get(self, request, **kwargs):
        if self.get_object().author == self.request.user:
            return DeleteView.get(self, request, **kwargs)
        else:
            messages.add_message(request, messages.WARNING, "Você pode deletar apenas seus próprios arquivos")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())


@login_required
def create_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        form.author = request.user
        if form.is_valid():
            pdf = form.save()
            return redirect(reverse_lazy('pdf_view', kwargs={'pk': pdf.pk}))
    else:
        form = PdfForm()
    return render(request, 'taverna_dos_pdfs/pdf_create.html', {'form': form})


@login_required
def up_vote(request, pk):
    pdf = PdfFile.objects.get(pk=pk)
    pdf.votes.up(request.user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def down_vote(request, pk):
    pdf = PdfFile.objects.get(pk=pk)
    pdf.votes.down(request.user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))