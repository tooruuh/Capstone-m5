from products.models import Product

# from products.serializers import ProductSerializer
from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Cart


class CartSerializer(serializers.Serializer):
    total_price = serializers.SerializerMethodField(read_only=True)
    total_itens = serializers.SerializerMethodField(read_only=True)

    user = UserSerializer(read_only=True)
    # products = ProductSerializer()

    def get_total_price(self, obj: Product):

        for item in obj:
            total_price += obj.price

        return total_price

    def get_total_itens(self, obj: Product):
        return len(Product)
