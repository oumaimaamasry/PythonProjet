from . import views
from django.urls import path

app_name = 'categorie'

urlpatterns = [
   path('categorie/', views.Categorie, name ='categorie'),
   path('ajouter_categorie/',views.ajouter_categorie,name='ajouter_categorie'),
   path('modifier_categorie/<str:pk>',views.modifier_categorie,name='modifier_categorie'),
   path('supprimer_categorie/<str:pk>',views.supprimer_categorie,name='supprimer_categorie'),


]


