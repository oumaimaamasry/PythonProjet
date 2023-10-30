from . import views
from django.urls import path

app_name = 'sous_categorie'

urlpatterns = [
   path('sous_categorie/', views.sous_cat, name ='sous_categorie'),
   path('ajouter_souscategorie/', views.ajouter_souscategorie, name='ajouter_souscategorie'),
   path('modifier_souscategorie/<str:pk>',views.modifier_souscategorie,name='modifier_souscategorie'),
   path('supprimer_souscategorie/<str:pk>',views.supprimer_souscategorie,name='supprimer_souscategorie'),
   path('afficher_souscategorie/',views.afficher_souscat,name='afficher_souscategorie'),
   path('ajouter_sous/',views.ajouter_sous,name='ajouter_sous'),
]