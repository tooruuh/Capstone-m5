from products.models import Product

# from products.serializers import ProductSerializer
from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        # read_only_fields = ["total_price", "total_itens"]

    total_price = serializers.SerializerMethodField(method_name="get_total_price")
    total_itens = serializers.SerializerMethodField(method_name="get_total_itens")

    user = UserSerializer(read_only=True)
    # products = ProductSerializer()

    def get_total_price(self, obj: Product):

        for item in obj:
            total_price += obj.price

        return total_price

    def get_total_itens(self, obj: Product):
        return len(Product)
