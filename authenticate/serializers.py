from rest_framework import serializers
from .models import CustomUser 

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'age', 'can_be_contacted', 'can_data_be_shared']

        def validate(self, data):
            if data['age'] < 15:
                raise serializers.ValidationError("Vous devez avoir au moins 15 ans")
            if not data['can_data_be_shared']:
                raise serializers.ValidationError("Vous devez accepter de partager vos données pour créer un compte.")
            return data