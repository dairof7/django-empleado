from django.db import models

# Create your models here.
class Prueba(models.Model):
    #CharField = mc
    #IntegerField = mint
    
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo
    