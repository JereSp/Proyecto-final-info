from rest_framework import serializers
from apps.backend.models.comentarios.model import Comentarios

class ComentariosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'