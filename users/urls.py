from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, CustomAuthToken

# routers
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('auth/', CustomAuthToken.as_view()),
    path('', include(router.urls))
]
