from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from django.shortcuts import get_object_or_404

from carts.models import Cart

from .permission import IsSuperUser
from .serializers import CartSerializer, CartDetailSerializer

class CartView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsSuperUser]

    queryset = Cart.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CartSerializer
        return CartDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user,is_finalized=False)

class CartBuyView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()

    lookup_url_kwarg = "cart_id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id,is_finalized=False)
