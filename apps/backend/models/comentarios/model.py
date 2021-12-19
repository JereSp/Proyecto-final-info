from django.db import models
from apps.users.models import User
from apps.backend.models.posts.model import Posts


class Comentarios (models.Model):
    usuario_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    posts_id = models.ForeignKey(Posts,on_delete=models.DO_NOTHING)
    comment = models.CharField('comment',max_length=255)
    creation_date = models.DateField(auto_now= True)
    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'
