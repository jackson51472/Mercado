from django.db import models
from django.utils.translation import gettext_lazy as _

class Pessoa(models.Model):

    
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11, unique=True)
    telefone = models.IntegerField(_('Telefone'), blank=True,null=True)
    senha = models.CharField(_('Senha'), blank=False, max_length=100)
    login = models.CharField(_('Login'), blank=False, max_length=100, unique=True)
    

    class Meta:    
        abstract = True
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas')
        ordering = ['id']

    def __str__(self):
        return self.nome 

class Cliente(Pessoa):


    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

class Cargo(models.Model):

    nome_cargo = models.CharField(_('Nome Cargo'), max_length=100)
    carga_horaria = models.DecimalField(_("Carga horária"), null=True,blank=False, max_digits=12, decimal_places=3)
    comissao = models.DecimalField(_("Comissão"), blank=False,max_digits=4, decimal_places=3)



    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')
    
    def __str__(self):
        return self.nome_cargo

class Funcionario(Pessoa):
    cargo = models.ForeignKey(Cargo, null=True, on_delete= models.SET_NULL)
    salario = models.DecimalField(_("Salario"), null=True, blank=False, max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('Funcionario')
        verbose_name_plural = _('Funcionarios')

    def __str__(self):
        return f"{self.nome} / {self.cargo}"

class Fornecedor(models.Model):
    nome = models.CharField(_('Nome'), max_length=12)
    cnpj = models.CharField(_('CNPJ'), max_length=14, unique=True)

    class Meta:
        verbose_name = _('Fornecedor')
        verbose_name_plural = _('Fornecedores')
        
    def __str__(self):
        return f"{self.nome}"
    
class Produto(models.Model):
    nome_produto =  models.CharField(_("Nome do Produto"), blank=False, max_length=50, unique=True,)
    preco = models.DecimalField(_("Preço"), null=True, blank=False, max_digits=8, decimal_places=2)
    peso = models.DecimalField(_("Peso"), null=True, blank=False, max_digits=8, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, blank=True, null=True, on_delete= models.SET_NULL)
    marca = models.CharField(_("Nome da Marca"), blank=True, null=True, max_length=50,)
    estoque = models.IntegerField(_('Estoque'))
    

    
    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __str__(self):
        return f"{self.nome_produto} / R${self.preco}"

class Pedido(models.Model):
    data_pedido = models.DateTimeField(_("Data do Pedido"), blank=False)

    FEITO = "Feito"
    FINALIZADO = "Finalizado"

    YEAR_IN_SCHOOL_CHOICES = [
        (FEITO, "Feito"),
        (FINALIZADO,"Finalizado"),
       
    ]

    status = models.CharField(
        choices=YEAR_IN_SCHOOL_CHOICES,
    )

    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')
    
    def __str__(self):
        return f"{self.data_pedido} / {self.status}"

class ItemPedido(models.Model):
    item = models.ForeignKey(Produto, blank=True, null=True, on_delete= models.SET_NULL)
    quantidade = models.IntegerField(_("Quantidade Pedida"))
    pedido = models.ForeignKey(Pedido , blank=True, null=True, on_delete= models.SET_NULL)

    class Meta:
        verbose_name = _('Item Pedido')
        verbose_name_plural = _('Items Pedido')

    def __str__(self):
        return f"Produto {self.item} / Quantidade: {self.quantidade}"
    
class Cartao(models.Model):

    numero = models.CharField(_('Número Cartão'), max_length=12,unique=True)
    senha = models.CharField(_('Senha Cartão'), max_length=200)  
    pessoa_Dona = models.ForeignKey(Cliente, blank=False, null=True, on_delete= models.SET_NULL)

    class Meta:
        verbose_name = _('Cartão')
        verbose_name_plural = _('Cartões')
    
    def __str__(self):
        return f"{self.numero}" 

class Endereco(models.Model):
    
    cep = models.IntegerField(_('CEP'),)
    logradouro = models.CharField(_('Logradouro'), max_length=200)
    complemento = models.CharField(_('Complemento'), max_length=200)
    numero = models.IntegerField(_('Número '), )
    bairro = models.CharField(_('Bairro'), max_length=200)
    cidade = models.CharField(_('Cidade'), max_length=200)
    pais = models.CharField(_('País'), max_length=200)
    utc = models.CharField(_('UTC'), max_length=200)
    endereco_fornecedor = models.ForeignKey(Fornecedor, blank=False, null=True, on_delete= models.SET_NULL)


    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')