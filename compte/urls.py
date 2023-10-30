from django.urls import path

from . import views

app_name = 'compte'

urlpatterns = [
   path('', views.inscription, name='inscription'),
   path('acces', views.acces, name='acces'),

]

