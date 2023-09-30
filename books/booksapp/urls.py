from django.urls import path,include
from .views import CustomUserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', CustomUserViewSet, 'booksapp')



urlpatterns = [
    path('', include(router.urls))
]