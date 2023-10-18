from django.contrib import admin 
from aplic.models import Cliente, Cargo, Funcionario, Cartao, ItemPedido, Pedido, Produto, Endereco, Fornecedor, Telefone, Mercado

   
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome_cargo', 'carga_horaria', 'comissao')

admin.site.register(Cartao)
class CartaoInline(admin.TabularInline):
    model = Cartao
    readonly_fields = ('id',)
    extra = 1
    classes = ('collapse', )
    list_display = ['numero_cartao',"pessoa_dona"]

admin.site.register(Produto)
class ProdutoInline(admin.TabularInline):
    model = Produto
    readonly_fields = ('id',)
    extra = 1
    classes = ('collapse', )
    list_display = ("nome_produto", "preco", "peso", "estoque", "fornecedor", "marca", )


admin.site.register(Endereco)
class EnderecoInline(admin.TabularInline):
    model = Endereco
    readonly_fields = ('id',)
    extra = 1
    classes = ('collapse', )
    list_display = ("cidade", "cep", "logradouro", "bairro", "numero_casa", "complemento",)


admin.site.register(ItemPedido)
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    readonly_fields = ('id',)
    extra = 1
    classes = ('collapse', )
    list_display = ("produto", "quantidade", "pedido", "valorPedido")
    readonly_fields = ('valorPedido',)


admin.site.register(Telefone)
class TelefoneInline(admin.TabularInline):
    list_display = ("numero_telefone", "telefone_fornecedor", "telefone_cliente", "telefone_funcionario",)
    model = Telefone   
    readonly_fields = ('id',)
    extra = 1 
    classes = ('collapse', )

@admin.register(Mercado)
class MercadpAdmin(admin.ModelAdmin):
    list_display = ("nome_mercado", "cnpj_mercado", "numero_telefone_mercado")

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("data_pedido", "status", "funcionario_pedido", "cliente_pedido",)
    inlines = [ItemPedidoInline, ]

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ("nome_fornecedor","cnpj",)
    inlines = [EnderecoInline, TelefoneInline, ]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [EnderecoInline, TelefoneInline, CartaoInline]
    list_display = ["nome", 'cpf', ]
    
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', "salario", 'cargo',]
    inlines = [EnderecoInline, TelefoneInline]
 