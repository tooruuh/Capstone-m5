from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    class Meta:
        model: Product
        fields = "__all__"
        
