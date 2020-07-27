from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from taverna_dos_pdfs.forms import RegistrationForm


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
    return render(request, 'registration/register_form.html', {'form': form})
