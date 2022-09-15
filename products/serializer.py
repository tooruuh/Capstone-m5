from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["seller"]
    
    def create(self, validated_data: dict):
        product = Product.objects.create(**validated_data)
        return product

    
