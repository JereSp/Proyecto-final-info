from rest_framework import serializers
from apps.backend.models.posts.model import Posts

class PostsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'