from django.contrib import admin
from aplic.models import Cliente, Cargo, Funcionario, Cartao, ItemPedido, Pedido, Produto, Endereco, Fornecedor, Telefone, Mercado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ["nome", 'cpf', ]
    
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome_cargo', 'carga_horaria', 'comissao')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):

    list_display = ['nome', 'cpf', "salario", 'cargo',]


@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ['numero_cartao',"pessoa_dona"]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome_produto", "preco", "peso", "estoque", "fornecedor", "marca", )

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("cidade", "cep", "logradouro", "bairro", "numero_casa", "complemento",  "pais", "uf", "endereco_fornecedor", "endereco_cliente", "endereco_funcionario",)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ("nome_fornecedor","cnpj",)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("data_pedido", "status", "funcionario_pedido", "cliente_pedido")

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):

    list_display = ("produto", "quantidade", "pedido", "valorPedido")
    readonly_fields = ('valorPedido',)


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ("numero_telefone", "telefone_fornecedor", "telefone_cliente", "telefone_funcionario",)


@admin.register(Mercado)
class MercadpAdmin(admin.ModelAdmin):
    list_display = ("nome_mercado", "cnpj_mercado", "numero_telefone_mercado")

