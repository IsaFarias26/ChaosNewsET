from django.contrib import admin
from .models import Categoria,Noticia, Comentarios

admin.site.register(Categoria)

class AdminNoticias(admin.ModelAdmin):
    list_display=('titulo','categoria','tiempo')

admin.site.register(Noticia,AdminNoticias)

class AdminComentario(admin.ModelAdmin):
    list_display=('noticias','email','comentario','estado')

admin.site.register(Comentarios,AdminComentario)


