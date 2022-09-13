from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from .permission import IsUserIsExact

from .models import Favorite
from .serializers import FavoriteSerializer, FavoriteDetailSerializer

class FavoriteView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Favorite.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return FavoriteSerializer
        return FavoriteDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class FavoriteDetailView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsUserIsExact]

    queryset = Favorite.objects.all()

    lookup_url_kwarg = "favorite_id"

