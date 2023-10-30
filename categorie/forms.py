from django.forms import ModelForm
from .models import categorie



class categorieform(ModelForm):
    class Meta:
        model=categorie
        fields='__all__'
