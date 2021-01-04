import django_filters
from django_filters import CharFilter
from .models import *


class ProductFilter(django_filters.FilterSet):

    #name = CharFilter(field_name='name', lookup_expr='icontains')
    #category = CharFilter(field_name='category', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = '__all__'
        exclude = 'image'