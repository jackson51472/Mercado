from django.contrib import admin
from aplic.models import Pessoa
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone')