from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from carts.models import Cart

from .permission import IsCartOwner
from .serializers import CartSerializer


class CartView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCartOwner]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
