from django.shortcuts import render, redirect
from .forms import ContactoForm


def home(request):
    return render(request, 'web/home.html')


def sobre_mi(request):
    return render(request, 'web/sobremi.html')


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')
    else:
        form = ContactoForm()

    return render(request, 'web/contacto.html', {'form': form})