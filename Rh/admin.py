from django.contrib import admin
from Rh.models import Funcionario, Departamento


class FuncionarioAdmin(admin.modeladmin):
    list_display = ['nome','departamento', 'cargo']
    list_filter = ['Departamento', 'Cargo']


# Register your models here.
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Departamento)