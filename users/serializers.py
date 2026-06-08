from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ImageManager, DocumentManager

class InscriptionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type':'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type':'password'}, label="Confirmation mot de passe")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': "Les mots de passe ne correspondnt pas."}
            )
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
        read_only_fields = fields

class ImageManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageManager
        fields = '__all__'

class DocumentManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentManager
        fields = '__all__'