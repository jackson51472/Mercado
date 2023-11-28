import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from stdimage.models import StdImageField
from django.contrib.auth.models import User

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return filename



class Cliente(models.Model):
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11, unique=True)
    

    # Para ser feito essa parte você deve importar User
    # from django.contrib.auth.models import User
    # Essa parte vincúla o cliente com o User que o ele criar na hora de cadastrar um novo Cliente no sistema 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #=========================================================================================================
    
    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome

class Pessoa(models.Model):   
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11, unique=True)

    

    class Meta:    
        abstract = True
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas')
        ordering = ['id']

    def __str__(self):
        return self.nome 

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
    nome_fornecedor = models.CharField(_('Nome'), max_length=12)
    cnpj = models.CharField(_('CNPJ'), max_length=14, unique=True)

    class Meta:
        verbose_name = _('Fornecedor')
        verbose_name_plural = _('Fornecedores')
        
    def __str__(self):
        return f"{self.nome_fornecedor}"
    
class Produto(models.Model):

    nome_produto =  models.CharField(_("Nome do Produto"), blank=False, max_length=50, unique=True,)
    preco = models.DecimalField(_("Preço"), null=True, blank=False, max_digits=8, decimal_places=2)
    peso = models.DecimalField(_("Peso"), null=True, blank=False, max_digits=8, decimal_places=2)

    GRAMA = "Grama"
    ML = "Ml"
    UNIDADE = "Quantidade"

    CHOICES = [
        (GRAMA, "Grama"),
        (ML,"Ml"),
        (UNIDADE,"Quantidade"),
       
    ]
    status = models.CharField(
        choices=CHOICES,
    )



    imagem = StdImageField(_('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    fornecedor = models.ForeignKey(Fornecedor, blank=True, null=True, on_delete= models.SET_NULL)
    marca = models.CharField(_("Nome da Marca"), blank=True, null=True, max_length=50,)
    estoque = models.IntegerField(_('Estoque'))
    

    
    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def dividir(self):
        quantidade = 0
        if self.peso >= 1000:
            quantidade = self.peso / 1000
        else:
            quantidade = self.peso


        #GRAMA
        if self.status == "Grama":
            if self.peso >= 1000:
                if (self.peso % 1000) != 0:
                    return f"{quantidade:.2f} kg"
                else:
                    return f"{quantidade:.0f} kg"
                
            else:
                return f"{quantidade:.0f} g"
        #ML    
        elif self.status == "Ml":
            if self.peso >= 1000:
                if (self.peso % 1000) != 0:
                    return f"{quantidade:.2f} L"
                else:
                    return f"{quantidade:.0f} L"
            else:
                return f"{quantidade:.0f} ml"
        #UNIDADE
        else:
            return ""




    def __str__(self):
        return f"{self.nome_produto} / R${self.preco}"

class Pedido(models.Model):
    data_pedido = models.DateTimeField(_("Data do Pedido"), blank=False)
    funcionario_pedido = models.ForeignKey(Funcionario, blank=False, null=True, on_delete= models.SET_NULL)
    cliente_pedido = models.ForeignKey(Cliente, blank=False, null=True, on_delete= models.SET_NULL)
    FEITO = "Feito"
    FINALIZADO = "Finalizado"
    ANDAMENTO = "Andamento"

    CHOICES = [
        (FEITO, "Feito"),
        (FINALIZADO,"Finalizado"),
        (ANDAMENTO,"Andamento"),
       
    ]
    status = models.CharField(
        choices=CHOICES,
    )



    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')
    
    def __str__(self):
        return f"{self.data_pedido} / {self.status}"

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, blank=True, null=True, on_delete= models.SET_NULL)
    quantidade = models.IntegerField(_("Quantidade Pedida"))
    pedido = models.ForeignKey(Pedido , blank=True, null=True, on_delete= models.SET_NULL)
    

    def valorPedido(self):
        return self.quantidade * self.produto.preco

    class Meta:
        verbose_name = _('Item Pedido')
        verbose_name_plural = _('Items Pedido')

    def __str__(self):
        return f"Produto {self.produto} / Quantidade: {self.quantidade}"
    
class Cartao(models.Model):

    numero_cartao = models.CharField(_('Número Cartão'), max_length=12,unique=True)
    pessoa_dona = models.ForeignKey(Cliente, blank=False, null=True, on_delete= models.SET_NULL)

    class Meta:
        verbose_name = _('Cartão')
        verbose_name_plural = _('Cartões')
    
    def __str__(self):
        return f"{self.numero_cartao}" 

class Endereco(models.Model):
    
    cidade = models.CharField(_('Cidade'), max_length=200)
    cep = models.CharField(_('CEP'),)
    logradouro = models.CharField(_('Logradouro'), max_length=200)
    complemento = models.CharField(_('Complemento'), max_length=200)
    numero_casa = models.CharField(_('Número '),)
    bairro = models.CharField(_('Bairro'), max_length=200)
    
    pais = models.CharField(_('País'), max_length=200)
    uf = models.CharField(_('UF'), max_length=200, blank=False, default=None)
    endereco_fornecedor = models.ForeignKey(Fornecedor, blank=True,  default=None, null=True, on_delete= models.SET_NULL)
    endereco_cliente = models.ForeignKey(Cliente, blank=True, default=None, null=True, on_delete= models.DO_NOTHING)
    endereco_funcionario = models.ForeignKey(Funcionario, blank=True, default=None, null=True, on_delete= models.SET_NULL)

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

    
    def __str__(self):
        return f"Cidade: {self.cidade} | Bairro: {self.bairro} | Rua: {self.logradouro}"

class Telefone(models.Model):
    numero_telefone = models.CharField(_('Número'), max_length=11)
    telefone_fornecedor = models.ForeignKey(Fornecedor, blank=True, default=None, null=True, on_delete= models.SET_NULL )
    telefone_cliente = models.ForeignKey(Cliente, blank=True, default=None, null=True, on_delete= models.DO_NOTHING)
    telefone_funcionario = models.ForeignKey(Funcionario, blank=True, default=None, null=True, on_delete= models.SET_NULL)



    class Meta:
        verbose_name = _('Telefone')
        verbose_name_plural = _('Telefones')
    
    def __str__(self):
        return f"Numero: {self.numero_telefone}"

class Mercado(models.Model):
    nome_mercado =  models.CharField(_("Nome do Mercado"), blank=False, max_length=50, unique=True,)
    cnpj_mercado = models.CharField(_('CNPJ'), max_length=14, unique=True)
    numero_telefone_mercado = models.CharField(_('Número'), max_length=11)    

    class Meta:
        verbose_name = _('Mercado')
        verbose_name_plural = _('Mercados')
    
    def __str__(self):
        return f"Mercado {self.nome_mercado}"

