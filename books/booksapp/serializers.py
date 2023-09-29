# from rest_framework import serializers
# from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'

from rest_framework import serializers
from .models import CustomBookUser  # Import your user model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomBookUser
        fields = ('id', 'email', 'is_active', 'is_staff')  # Add other fields as needed

    # You can add extra validation or customization here if necessary
