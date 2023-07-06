from django.urls import path
from . import views
from app.views import index
from app.views import iniciosesion
from app.views import carrito
from app.views import contacto
from app.views import Login
from app.views import RegistrarUsuario

urlpatterns = [
    path('', views.index, name='index'),
    path('app/iniciosesion.html', views.iniciosesion, name='iniciosesion'),
    path('app/Carrito.html', views.carrito, name='Carrito'),
    path('app/Contact.html', views.contacto, name='Contact'),
    path('app/Login.html', views.Login, name='Login'),
    path('app/RegistrarUsuario.html', views.RegistrarUsuario, name='RegistrarUsuario'),
] 