from django.shortcuts import render, redirect
from .forms import *


# Create your views here.


def index(request):
    form = Contactform
    if request.method == 'POST':
        form = Contactform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('index')

    data = {

        'form': form,

    }
    return render(request, 'pages/home/home.html', data)
