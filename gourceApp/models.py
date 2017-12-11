from django.db import models
from colorfield.fields import ColorField
from gourceApp.choices import *
from decimal import Decimal

class Hierarquia(models.Model):
    name = models.CharField(max_length=200)

class Arvore(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    escola = models.CharField(max_length=200, verbose_name='Escola')
    serie = models.CharField(choices=SERIES, max_length=200, verbose_name='Série', default='-')
    cidade = models.CharField(max_length=200, verbose_name='Cidade')

    class Meta:
        db_table = 'arvore'

class Gource(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    cor = ColorField(default='#000000', verbose_name='Cor de fundo')
    fonte = models.PositiveIntegerField(verbose_name='Tamanho da fonte')
    elasticidade = models.DecimalField(verbose_name='Elasticidade', max_digits=2, decimal_places=1, default='0.5')

    class Meta:
        db_table = 'gource'
