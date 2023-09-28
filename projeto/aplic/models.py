from django.db import models
from django.utils.translation import gettext_lazy as _

class Pessoa(models.Model):

    
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11,)
    telefone = models.IntegerField(_('Telefone'), blank=True,)
    senha = models.CharField(_('Senha'), blank=False, max_length=100)
    login = models.CharField(_('Login'), blank=False, max_length=100)
    

    class Meta:    
        abstract = True
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas')
        ordering = ['id']

    def __str__(self):
        return self.nome

class Cartao(models.Model):
    numero = models.CharField(_('Número Cartão'), max_length=12)
    senha = models.CharField(_('Senha Cartão'), max_length=200)

    class Meta:
        verbose_name = _('Cartão')
        verbose_name_plural = _('Cartões')
    
    def __str__(self):
        return f"{self.numero}"
    
class Endereco(models.Model):
    cep = models.CharField(_('CEP'), max_length=8)
    logradouro = models.CharField(_('Logradouro'), max_length=200)
    complemento = models.CharField(_('Complemento'), max_length=200)
    numero = models.CharField(_('Número '), max_length=4)
    bairro = models.CharField(_('Bairro'), max_length=200)
    cidade = models.CharField(_('Cidade'), max_length=200)
    pais = models.CharField(_('País'), max_length=200)
    utc = models.CharField(_('UTC'), max_length=200)

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')
    

class Cliente(Pessoa):
    cartao = models.ForeignKey(Cartao, null=True, on_delete= models.SET_NULL)

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

class Produto(models.Model):
    preco = models.DecimalField(_("Preço"), null=True, blank=False, max_digits=8, decimal_places=2)
    peso = models.DecimalField(_("Peso"), null=True, blank=False, max_digits=8, decimal_places=2)
    marca = models.CharField(_("Nome da Marca"), blank=False, max_length=50,)
    estoque = models.IntegerField(_('Número Cartão'))
    nome_produto =  models.CharField(_("Nome do Produto"), blank=False, max_length=50,)
    
    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __str__(self):
        return f"{self.nome_produto} {self.preco}R$"

class Fornecedor(models.Model):
    nome = models.CharField(_('Nome'), max_length=12)
    cnpj = models.CharField(_('CNPJ'), max_length=14)

    class Meta:
        verbose_name = _('Fornecedor')
        verbose_name_plural = _('Fornecedores')