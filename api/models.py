from django.db import models
import uuid
from django.contrib.auth.models import User

class Nature(models.TextChoices):
    LANGUAGE = "language", "Language"
    FRAMEWORK = "framework", "Framework"
    AUTRE = "autre", "Autre"

class Cour(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=50)
    extension = models.CharField(max_length=20)
    description = models.TextField()
    nature = models.CharField(max_length=20, choices=Nature.choices, default=Nature.AUTRE)
    actif = models.BooleanField(default=True)
    like = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cours")

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=['name','extension'],
                name='unique_name_extension'
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.extension}"