from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from sous_categorie.models import sous_categorie

class materiel(models.Model):
    STATUS= (
        ('Aucun','Aucun'),
         ('Très bon','Très bon'),
         ('Bon','Bon'),
         ('Moyen','Moyen'),
        ('Mauvais','Mauvais'),
        ('En panne','En panne')
    )
    Type= models.ForeignKey(sous_categorie, null=True, on_delete=models.SET_NULL)
    Numero_inventaire=models.TextField(max_length=30, null=True)
    Numero_serie = models.TextField(max_length=30, null=True)
    Marque = models.TextField(max_length=30, null=True)
    Model = models.TextField(max_length=30, null=True)
    Etat = models.TextField(max_length=30,choices=STATUS)
    #Images = models.ImageField(upload_to="static/images", blank=True, null=True)
    Date_acquisition = models.DateTimeField(null=True)

    def __str__(self):
        return self.Marque
