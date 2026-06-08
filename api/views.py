from django.shortcuts import render
from rest_framework import viewsets
from .models import Cour
from django.contrib.auth.models import User
from .serializers import UserSerializer, CourSerializer
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

class CourViewSet(viewsets.ModelViewSet):
    queryset = Cour.objects.all()
    serializer_class = CourSerializer
    lookup_field = "uuid"

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]