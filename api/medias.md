Oui, si tu as déjà fait :

- ✅ PostgreSQL
- ✅ Variables d'environnement (`python-decouple` ou `django-environ`)
- ✅ CORS
- ⬜ Médias et fichiers uploadés

alors il te reste essentiellement la gestion des fichiers.

## 1. Ajouter un champ de fichier dans un modèle

Exemple pour une image :

```python
from django.db import models

class Cour(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='cours/images/',
        blank=True,
        null=True
    )
```

Ou pour un document :

```python
document = models.FileField(
    upload_to='cours/documents/',
    blank=True,
    null=True
)
```

---

## 2. Installer Pillow (pour les images)

```bash
pip install Pillow
```

Les `ImageField` en ont besoin.

---

## 3. Configurer les médias dans `settings.py`

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 4. Configurer les URLs

Dans le fichier principal `urls.py` :

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # tes urls
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
```

---

## 5. Créer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Tester avec l'admin Django

Si ton modèle est enregistré dans l'admin :

```python
from django.contrib import admin
from .models import Cour

admin.site.register(Cour)
```

Lance :

```bash
python manage.py createsuperuser
python manage.py runserver
```

Va sur :

```text
http://127.0.0.1:8000/admin
```

et essaye d'uploader une image ou un document.

---

## 7. Avec Django REST Framework

Si tu exposes l'image dans une API :

```python
class CourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cour
        fields = '__all__'
```

Le JSON renverra automatiquement :

```json
{
  "id": 1,
  "name": "Python",
  "image": "/media/cours/images/python.png"
}
```

---

## Vérification finale

Quand tu uploades un fichier :

```text
media/
└── cours/
    ├── images/
    │   └── photo.png
    └── documents/
        └── cours.pdf
```

et l'URL :

```text
http://127.0.0.1:8000/media/cours/images/photo.png
```

doit afficher le fichier.

C'est généralement ce qu'on attend quand une checklist Django mentionne **"Médias et fichiers uploadés (images, documents)"**. Une fois qu'un upload fonctionne et que les fichiers sont servis correctement, cette partie peut être considérée comme terminée. 🚀
