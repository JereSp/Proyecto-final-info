from apps.backend.models.posts.model import Posts
from apps.backend.models.posts.serializer import PostsSerializer
from rest_framework.viewsets import ModelViewSet

class PostsAPIView(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer