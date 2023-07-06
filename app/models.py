from django.db import models

class Categoria(models.Model):
    titulo=models.CharField(max_length=200)
    categoria_imagen=models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    titulo=models.CharField(max_length=300)
    imagen=models.ImageField(upload_to='imgs/')
    detalle=models.TextField()
    tiempo=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Noticias'

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    noticias=models.ForeignKey(Noticia,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comentario=models.TextField()
    estado=models.BooleanField(default=False)

    def __str__(self):
        return self.comentario