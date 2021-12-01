from rest_framework import serializers
from .models import *
from rest_framework import serializers


class BotSerializer(serializers.Serializer):
    api_key = serializers.CharField()
    api_secret = serializers.CharField()
    quantity = serializers.FloatField()
    pair = serializers.ListField(
        child=serializers.CharField()
    )


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["api_key", "api_secret"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
