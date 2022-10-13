from rest_framework import status, viewsets  # noqa
from rest_framework.response import Response  # noqa
from rest_framework.permissions import IsAuthenticated, AllowAny  # noqa

from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)
