from django.contrib import admin
from aplic.models import Cliente, Cargo, Funcionario
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['cartao','nome','cpf','login','senha','telefone']
    
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome_cargo', 'salario', 'comissao')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['cargo','nome','cpf','login','senha','telefone']