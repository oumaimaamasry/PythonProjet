from django.forms import ModelForm
from .models import sous_categorie



class sous_categorieform(ModelForm):
    class Meta:
        model=sous_categorie
        fields='__all__'
