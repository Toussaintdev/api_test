from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cour

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

class CourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cour
        fields = ["uuid", "name", "extension", "description", "nature", "actif", "like", "auteur"]
        read_only_fields = ["uuid", "actif", "like", "auteur"]