from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        # ordena por el nombre y con -name ordena descendente
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad



class Empleado(models.Model):
    job_list = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Ingeniero'),
        ('3','Desarrollador'),
    )
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombre Completo', max_length=100, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=job_list)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    # imagen = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        # ordena por el nombre y con -name ordena descendente
        ordering = ['-first_name', 'last_name']

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name