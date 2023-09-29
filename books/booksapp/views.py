
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import CustomUser
# from .serializers import UserSerializer
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST

# # Create your views here.

# class AccViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer

from rest_framework import viewsets, permissions
from .models import CustomBookUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomBookUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # You can add custom methods or overrides here if needed
