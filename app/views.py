from django.shortcuts import render
from .models import Noticia

def index(request):

    return render(request, 'app/index.html', {})

def iniciosesion(request):
    return render(request, 'app/iniciosesion.html', {})

def carrito(request):
    return render(request, 'app/Carrito.html', {})

def contacto(request):
    return render(request, 'app/Contact.html', {})

def Login(request):
    return render(request, 'app/Login.html', {})

def RegistrarUsuario(request):
    return render(request, 'app/RegistrarUsuario.html', {})

#def noticia_list(request):
    #noticias = Noticia.objects
    #return render(request, 'app/index.html', {'Noticia': noticias})