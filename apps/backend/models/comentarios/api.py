from apps.backend.models.comentarios.model import Comentarios
from apps.backend.models.comentarios.serializer import ComentariosSerializer
from rest_framework.viewsets import ModelViewSet

class ComentariosAPIView(ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer