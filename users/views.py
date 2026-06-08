from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from .serializers import InscriptionSerializer, ProfilSerializer, ImageManagerSerializer, DocumentManagerSerializer
from .models import ImageManager, DocumentManager

# Create your views here.

class InscriptionView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = InscriptionSerializer
    permission_classes = [permissions.AllowAny]

class ProfilView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class ExempleViewSet(viewsets.ModelViewSet):
    # queryset
    # serializer_class
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class ImageManagerViewSet(viewsets.ModelViewSet):
    queryset = ImageManager.objects.all()
    serializer_class = ImageManagerSerializer
    # permission_classes = [permissions.AllowAny]

class DocumentManagerViewSet(viewsets.ModelViewSet):
    queryset = DocumentManager.objects.all()
    serializer_class = DocumentManagerSerializer