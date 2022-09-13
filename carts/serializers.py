
# from products.serializers import ProductSerializer
from asyncore import read
from rest_framework import serializers
from products.serializer import ProductSerializer
from users.serializers import UserSerializer

from .models import Cart
from .exceptions import ValidationDuplicatedProduct, ValidationIsSelled
from products.models import Product
from users.models import User


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        carts = Cart.objects.filter(user=validated_data["user"])

        for cart in carts:
            if cart.product == validated_data["product"]:
                raise ValidationDuplicatedProduct("this product is already added to your cart")
            if validated_data["product"].is_active == False:
                raise ValidationIsSelled("Product is sold")
        cart = Cart.objects.create(**validated_data)
        
        return cart

class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        read_only_fields = ["user"]
    product = ProductSerializer(read_only=True)
    
    def update(self, instance, validated_data: dict):
        print(instance)
        import ipdb

        ipdb.set_trace()
        # for product in products:
        #     product.is_finalized
