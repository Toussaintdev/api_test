from django.contrib import admin
from .models import ImageManager,  DocumentManager

# Register your models here.

admin.site.register([ImageManager, DocumentManager])