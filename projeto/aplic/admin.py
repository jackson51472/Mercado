from django.contrib import admin
from aplic.models import Cliente, Cargo, Funcionario, Cartao, ItemPedido, Pedido, Produto, Endereco, Fornecedor

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", 'cpf', 'login', 'senha', 'telefone']
    
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome_cargo', 'carga_horaria', 'comissao')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', "salario", 'cargo', 'telefone', 'login', 'senha',]

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ['numero','senha',"pessoa_Dona"]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome_produto", "preco", "peso", "estoque", "fornecedor", "marca", )

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("endereco_fornecedor","cidade", "cep", "logradouro", "bairro", "numero", "complemento",  "pais", "uf")

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ("nome","cnpj",)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("data_pedido", "status", "funcionario_pedido", "cliente_pedido")

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("item", "quantidade", "pedido", "valorTotal")
    readonly_fields = ('valorTotal',)
