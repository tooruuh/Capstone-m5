from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminOrReadOnly

class UserView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
