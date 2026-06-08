from django.db import models

# Create your models here.

def upload_path_img(instance, filename):
    ext = filename.split('.')[-1]
    new_name = f"{instance.name}_file.{ext}"
    return f"imagemanager/images/{new_name}"

def upload_path_doc(instance, filename):
    ext = filename.split('.')[-1]
    new_name = f"{instance.titre}_file.{ext}"
    return f"imagemanager/documents/{new_name}"

class ImageManager(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=upload_path_img,
        blank=True,
        null=True
    )

class DocumentManager(models.Model):
    titre = models.CharField(max_length=100)
    document = models.FileField(
        upload_to=upload_path_doc,
        null=True,
        blank=True
    )