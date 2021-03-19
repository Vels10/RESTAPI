from api.models import api
from rest_framework import viewsets, permissions
from .serializers import APISerializer

class APIViewSet(viewsets.ModelViewSet):
    queryset = api.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = APISerializer