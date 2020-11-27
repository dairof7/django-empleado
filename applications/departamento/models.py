from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, )
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    is_active = models.BooleanField('Activo', default=True)
    
    class Meta:
        verbose_name = 'Departamentos'
        verbose_name_plural = 'Areas - Departamentos'
        # ordena por el nombre y con -name ordena descendente
        ordering = ['-name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.short_name
