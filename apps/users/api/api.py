from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet

class UserAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer