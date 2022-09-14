from rest_framework import serializers

from carts.models import Cart
from django.shortcuts import get_object_or_404
# from carts.serializers import CartDetailSerializer

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name","email","password","plan","wallet","updated_at","created_at"]
        extra_kwargs = {
            "password": {"write_only": True},
            "wallet": {"read_only": True}
        }
    
    def create(self, validated_data: dict):
        validated_data["username"] = validated_data["email"]
        user = User.objects.create_user(**validated_data)
        return user
        
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)