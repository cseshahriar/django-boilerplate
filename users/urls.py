from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, CustomAuthToken, LogoutApiView

# routers
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('auth/', CustomAuthToken.as_view()),
    path('', include(router.urls)),
    path('logout/', LogoutApiView.as_view()),
]
