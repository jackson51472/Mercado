from django.db import models
from django.utils.translation import gettext_lazy as _

class Pessoa(models.Model):
    
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11,)
    telefone = models.IntegerField(_('Telefone'), blank=True,)
    senha = models.CharField(_('Senha'), blank=False, max_length=100)
    login = models.CharField(_('Login'), blank=False, max_length=100)
    
    def alterar_nome(self):
        novo_nome = models.CharField(_("Nome"), blank=False, max_length=50,)
        self.nome = novo_nome
    
    def alterar_login(self):
        novo_login = models.CharField(_('Login'), blank=False, max_length=100)
        self.login = novo_login
        
    def alter_senha(self):
        nova_senha = models.CharField(_('Senha'), blank=False, max_length=100)
        self.senha = nova_senha
        
    def adicionar_telefone(self):
        novo_telefone = models.IntegerField(_('Telefone'), blank=True,)

    class Meta:    
        abstract = True
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas')
        ordering = ['id']

    def __str__(self):
        return self.nome

class Cliente(Pessoa):
    cartao = models.CharField(_('Cartão'), max_length=20)

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')


class Cargo(models.Model):
    nome_cargo = models.CharField(_('Nome Cargo'), max_length=100)
    salario = models.DecimalField(_("Salario"), blank=False, max_digits=12, decimal_places=3)
    comissao = models.DecimalField(_("Comissão"), blank=False,max_digits=4, decimal_places=3)



    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')
    
    def __str__(self):
        return self.nome_cargo
class Funcionario(Pessoa):
    cargo = models.ForeignKey(Cargo, null=True, on_delete= models.SET_NULL)

    class Meta:
        verbose_name = _('Funcionario')
        verbose_name_plural = _('Funcionarios')

    def __str__(self):
        return f"{self.nome} / {self.cargo}"

class Cartao(models.Model):
    numero = models.CharField(_('Número Cartão'), max_length=12)
    senha = models.CharField(_('Senha Cartão'), max_length=200)

    class Meta:
        verbose_name = _('Cartão')
        verbose_name_plural = _('Cartões')
    
    def __str__(self):
        return f"{self.numero}"
