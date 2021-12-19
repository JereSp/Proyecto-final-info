from apps.backend.models.categorias.model import Categorias
from apps.backend.models.categorias.serializer import CategoriasSerializer
from rest_framework.viewsets import ModelViewSet

class CategoriasAPIView(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer