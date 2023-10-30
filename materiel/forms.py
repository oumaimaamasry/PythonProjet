from django.forms import ModelForm
from .models import materiel



class materielform(ModelForm):
    class Meta:
        model=materiel
        fields='__all__'
