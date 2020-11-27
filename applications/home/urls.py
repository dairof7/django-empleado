from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('pruebalist/', views.PruebaListView.as_view()),
    path('pruebalistdb/', views.PruebaDBListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
] 