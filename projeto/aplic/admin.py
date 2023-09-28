from django.contrib import admin
from aplic.models import Cliente, Cargo, Funcionario, Cartao,Produto
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['cartao','nome','cpf','login','senha','telefone']
    
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome_cargo', 'carga_horaria', 'comissao')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'login', 'senha', 'telefone', "salario", 'cargo',]

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ['numero','senha']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome_produto", "marca", "estoque", "peso", "preco")