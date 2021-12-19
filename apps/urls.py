from django.db import router
from django.urls import path,include
from apps.users.api.api import UserAPIView
from apps.backend.models.categorias.api import CategoriasAPIView
from rest_framework import routers
from apps.backend.models.posts.api import PostsAPIView
from apps.backend.models.comentarios.api import ComentariosAPIView

router = routers.DefaultRouter()
router.register('usuarios',UserAPIView,basename='')
router.register('categorias',CategoriasAPIView,basename='')
router.register('posts',PostsAPIView)
router.register('comentarios',ComentariosAPIView)

urlpatterns = [
    path('', include(router.urls)),
]