from django.urls import path, include
from .views import InscriptionView, ProfilView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from .views import ImageManagerViewSet, DocumentManagerViewSet

router = routers.DefaultRouter()
router.register(r'img', ImageManagerViewSet)
router.register(r'doc', DocumentManagerViewSet)


urlpatterns = [
    path('inscription/', InscriptionView.as_view()),
    path('connexion/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('profil/', ProfilView.as_view()),
    path('images/', include(router.urls)),
]