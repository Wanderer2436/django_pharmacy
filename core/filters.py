import django_filters
import core.models


class ProductFilter(django_filters.FilterSet):
    name = django_filters.Filter(lookup_expr='icontains', label='Название:')
    manufacturer = django_filters.ChoiceFilter(label='Производитель:')
    price = django_filters.RangeFilter()
    country = django_filters.ChoiceFilter(label='Страна:')

    class Meta:
        model = core.models.Product
        fields = ('name', 'manufacturer', 'price', 'country',)
