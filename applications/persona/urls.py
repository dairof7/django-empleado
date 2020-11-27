from django.contrib import admin
from django.urls import path
from . import views

# app_name is the name of the urls for this app in django
app_name = 'persona_app'

urlpatterns = [
    path('list-all-empleado/', views.ListAllEmpleados.as_view()),
    # create a <area> variable to read data
    path('list-by-area-empleado/<area>', views.ListByAreaEmpleados.as_view()),
    path('list-by-kword-empleado/', views.ListByKwordEmpleados.as_view()),
    path('list-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    #detailView only allow pk
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('create-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='update_empleado'),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name='delete_empleado'),
] 
