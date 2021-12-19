from rest_framework import serializers
from apps.backend.models.categorias.model import Categorias

class CategoriasSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'