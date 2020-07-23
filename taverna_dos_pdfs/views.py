from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from taverna_dos_pdfs.forms import PdfForm, RegistrationForm
from taverna_dos_pdfs.models import PdfFile


def pdf_list(request):
    pdfs = PdfFile.objects.filter(deleted_at__isnull=True).order_by('votes')
    return render(request, 'taverna_dos_pdfs/pdf_list.html', {'pdfs': pdfs})


@login_required
def create_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
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


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Login incorreto ')

    else:
        return render(request, 'registration/login.html', {})


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
