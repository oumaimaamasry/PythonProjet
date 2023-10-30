from . import views
from django.urls import path

app_name = 'materiel'

urlpatterns = [
   path('materiel', views.Materiel, name = 'materiel'),
   path('ajouter_materiel', views.ajouter_materiel, name = 'ajouter_materiel'),
   path('modifier_materiel/<str:pk>',views.modifier_materiel,name='modifier_materiel'),
   path('supprimer_materiel/<str:pk>',views.supprimer_materiel,name='supprimer_materiel'),
   path('afficher_materiel/',views.afficher_mat,name='afficher_materiel'),
]
