from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password","plan","wallet","updated_at","created_at"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data)
        return user