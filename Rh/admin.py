from django.contrib import admin
from Rh.models import Funcionario, Departamento


class FuncionarioAdmin(admin.modeladmin):
    list_display = ['nome','departamento', 'cargo']
    list_filter = ['Departamento', 'Cargo']


# Registre seus modelos aqui
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Departamento)