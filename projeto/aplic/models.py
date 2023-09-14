from django.db import models
from django.utils.translation import gettext_lazy as _

class Pessoa(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11)
    telefone = models.CharField(_('telefone'), blank=True, max_length=200)

    class Meta:
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas')
        ordering = ['id']

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=500)
    carga_horaria = models.IntegerField(_('Carga Horária'))
    #imagem = StdImageField(_('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})


    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.nome
