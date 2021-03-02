from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/loginform')
def index(request):

    return render(request, "index.html")


def login(request):
    return render(request, "login/login.html")


def cargacards(request):
    return render(request, "cargacard.html")