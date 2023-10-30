from urllib import request
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from categorie.models import categorie


class sous_categorie(models.Model):
    Categorie= models.ForeignKey(categorie, null=True, on_delete=models.SET_NULL)
    Nom = models.TextField(max_length=30, null=True)

    def __str__(self):
        return self.Nom

