import django_filters
import core.models


class ProductFilter(django_filters.FilterSet):
    name = django_filters.Filter(lookup_expr='icontains', label='Название:')
    price = django_filters.RangeFilter()

    class Meta:
        model = core.models.Product
        fields = ('name', 'price',)


class PharmacyFilter(django_filters.FilterSet):
    street = django_filters.Filter(lookup_expr='icontains', label='Адрес:')

    class Meta:
        model = core.models.Pharmacy
        fields = ('street',)
