from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento
# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        # we can access and create a instance like this
        departamento = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )
        departamento.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']

        # we can access and create a instance like this
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            # select 1 just for default
            job='1',
            departamento=departamento
        )
        return super().form_valid(form)
