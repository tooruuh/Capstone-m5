from select import select
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .custom_permissions import IsSellerIsExact, IsSellerOrReadOnly

from .serializer import ProductSerializer
from .models import Product

class ProductGenericView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True)
        
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerIsExact]
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_url_kwarg = "product_id"