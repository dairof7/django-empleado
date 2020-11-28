from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm
# Create your views here.

class PruebaView(TemplateView):
    template_name = "home/prueba.html"

class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"


class PruebaListView(ListView):

    #puedo usar directamente un modelo de una base de datos o bien hacer un queryset
    queryset = ['1','2','3','4']
    # listnum este corresponde a la variable que voy a enviar-usar al html, con los datos de la queryset
    context_object_name = 'listnum'
    template_name = "home/lista.html"

class PruebaDBListView(ListView):

    model = Prueba
    # listnum este corresponde a la variable que voy a enviar-usar al html, con los datos de la queryset
    context_object_name = 'lista'
    template_name = "home/listadb.html"

# nos permite registrar datos en el modelo
class PruebaCreateView(CreateView):
    model = Prueba
    form_class = PruebaForm
    template_name = "home/add.html"
    success_url = '/'
    