from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    #model return the complete list of the model
    #num data to print each page
    paginate_by = 4
    #we can use the key word ?page=num in browser to select the page to print
    ordering = 'first_name'
    model = Empleado
    

class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_by_area.html'
    # one of the worst way to make a filter
    # queryset = Empleado.objects.filter(departamento__short_name='Ventas')

    def get_queryset(self):
        #reading the variable written on browser
        area = self.kwargs['area']
        # filter the Empleado using the short_name of departamento table
        lista = Empleado.objects.filter(departamento__short_name=area)
        return lista

class ListByKwordEmpleados(ListView):
    template_name = 'persona/list_by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        # use the request GET method and get the data 'kword'
        dato = self.request.GET.get("kword",)
        lista = Empleado.objects.filter(first_name=dato)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        if self.request.GET.get("id",):
            # get a empleado by id
            id = self.request.GET.get("id",)
            # empleado = Empleado.objects.get(id=id)
            # print(empleado)
            try:
                empleado = Empleado.objects.get(id=id)
                # get all habilidades with the many to many field with all() method
                habilidades = empleado.habilidades.all()
                return habilidades
            except:
                return ['No existe empleados con ese id']
        return []

    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    context_object_name = 'empleado'
    


    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'empleado del mes'
        return context
    


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/create_persona.html"
    # create view need the fields of the model to be created
    # fields = ['first_name', 'last_name', 'job'] or ['__all__']
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    # we must add a redirection in a create view, in this case '.' redirect to the same page
    # success_url = '.'
    # or we can use reverse_lazy and the app name + url name
    success_url = reverse_lazy('persona_app:success')

    # use this method to verify if input data for model is valid
    # form is the django form used in the template

    def form_valid(self, form):
        # as we are not using fullname in the form, we will concatenate and save it in DB here
        empleado = form.save(commit=False)
        # this is a bad practice because we save it 2 times but you can do it, well with commit=false you save it only one but is bad practice
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        # this is suggest of django documentation
        return super().form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:success')
    
    # the execution order of the method is, first post then form_valid

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # here we can get data of the POST and proccess it
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super().form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:success')
