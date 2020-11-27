from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):

    #list if display items in admin

    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    #if you want to add new field and its does not exist on model
    #create this function with the same name of the filed
    #obj contains all information of model
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name


    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades', 'departamento')
    #add a horizontal filter, its only allowed with relations
    filter_horizontal = ('habilidades',)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)