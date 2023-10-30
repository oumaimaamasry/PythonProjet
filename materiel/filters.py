import django_filters
from .models import materiel


class materielfiltre(django_filters.FilterSet):
    class Meta:
        model=materiel
        fields='__all__'