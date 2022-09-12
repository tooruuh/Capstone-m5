from rest_framework import serializers
from products.serializer import ProductSerializer
from users.serializers import UserSerializer

from .models import Favorite
from carts.exceptions import ValidationDuplicatedProduct, ValidationIsSelled


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        favorites = Favorite.objects.filter(user=validated_data["user"])

        for favorite in favorites:
            if favorite.product == validated_data["product"]:
                raise ValidationDuplicatedProduct("this product is already added to your favorites")
        favorite = Favorite.objects.create(**validated_data)
        
        return favorite

class FavoriteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"
        read_only_fields = ["user"]
    product = ProductSerializer(read_only=True)