from django.db import models

# Create your models here.
class ModelBase(models.Model):
    state = models.BooleanField(verbose_name='Estado', default=True)
    created_date = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(verbose_name='Fecha de Actualización', auto_now_add=False, auto_now=True)
    deleted_date = models.DateTimeField(verbose_name='Fecha de Eliminación', auto_now_add=False, auto_now=True)
    created_by = models.TextField(verbose_name='Creado por', max_length=30)
    updated_by = models.TextField(verbose_name='Actualizado por', max_length=30)
    deleted_by = models.TextField(verbose_name='Eliminado por', max_length=30)

    class Meta:
        abstract = True
        verbose_name = 'ModelBase'
        verbose_name_plural = 'ModelBase'
