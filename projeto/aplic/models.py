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