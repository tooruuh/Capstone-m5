from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .custom_permissions import IsSellerIsExact, IsSellerOrReadOnly

from .serializer import ProductSerializer
from .models import Product


class ProductGenericView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerOrReadOnly]
    
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        return ProductSerializer
    
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
        
        
class ProductDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerIsExact]
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_url_kwarg = "product_id"