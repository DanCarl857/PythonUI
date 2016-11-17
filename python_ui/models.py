# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Table1(models.Model):
    id_modelo = models.IntegerField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    nid = models.IntegerField(blank=True, null=True)
    gondola = models.CharField(max_length=64, blank=True, null=True)
    producto = models.CharField(max_length=159, blank=True, null=True)
    categoria_ipc = models.CharField(max_length=8, blank=True, null=True)
    categoria_ipc_9 = models.CharField(max_length=9, blank=True, null=True)
    des_producto = models.CharField(max_length=46, blank=True, null=True)
    contenido = models.CharField(max_length=5, blank=True, null=True)
    divisor = models.CharField(max_length=5, blank=True, null=True)
    multiplo = models.CharField(max_length=4, blank=True, null=True)
    unidades = models.CharField(max_length=3, blank=True, null=True)
    descripcion1 = models.CharField(max_length=13, blank=True, null=True)
    descripcion2 = models.CharField(max_length=18, blank=True, null=True)
    descripcion3 = models.CharField(max_length=10, blank=True, null=True)
    unidadmedida = models.CharField(max_length=8, blank=True, null=True)
    des_marca = models.CharField(max_length=21, blank=True, null=True)
    des_empresa = models.CharField(max_length=40, blank=True, null=True)
    campo = models.CharField(max_length=13, blank=True, null=True)
    nombre = models.IntegerField(blank=True, null=True)
    target = models.CharField(max_length=8, blank=True, null=True)
    likelihood = models.DecimalField(max_digits=9, decimal_places=8, blank=True, null=True)
    timestamp = models.CharField(max_length=20, blank=True, null=True)
    features = models.CharField(max_length=8, blank=True, null=True)
    modelo = models.CharField(max_length=16, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TABLE 1'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
