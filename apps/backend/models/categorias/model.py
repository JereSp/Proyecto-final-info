from django.db import models

class Categorias (models.Model):
    name = models.CharField('name',max_length=255)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        return self.name