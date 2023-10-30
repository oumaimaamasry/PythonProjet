from urllib import request
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class categorie(models.Model):
    Categorie = models.TextField(max_length=30, null=True)

    def __str__(self):
        return self.Categorie

