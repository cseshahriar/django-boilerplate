from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet

# routers
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/auth/', obtain_auth_token),
    path('', include(router.urls))
]
