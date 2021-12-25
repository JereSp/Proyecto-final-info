from django.db import models
from apps.users.models import User
from apps.backend.models.categorias.model import Categorias 

class Posts (models.Model):
    usuario_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    categoria_id = models.ForeignKey(Categorias,on_delete=models.DO_NOTHING)
    title = models.CharField('title',max_length=255)
    date = models.DateField(auto_now= True)
    content = models.CharField('content',max_length=510)
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
