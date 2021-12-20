from django.db import router
from django.urls import path,include
from apps.users.api.api import UserAPIView,LoginAPIView,RegisterAPIView
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
    path('login/',LoginAPIView,name = 'login_api'),
    path('register/', RegisterAPIView, name="register_api")
]