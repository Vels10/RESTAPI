from rest_framework import serializers
from api.models import api

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = api
        fields = '__all__'