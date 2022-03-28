from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
import core.models
import core.filters


class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'


class ProductList(TitleMixin, ListView):
    title = 'Товары'
    context_object_name = 'products'

    def get_filters(self):
        return core.filters.ProductFilter(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = core.models.Category.objects.all()
        context['filters'] = self.get_filters()
        return context

    def get_queryset(self):
        if not self.kwargs:
            qs = self.get_filters().qs
        else:
            qs = self.get_filters().qs.filter(category_id=self.kwargs['category_id'])
        return qs


class ProductDetail(TitleMixin, DetailView):
    model = core.models.Product
    title = 'Товар'


class PharmacyList(TitleMixin, ListView):
    title = 'Аптеки'

    def get_filters(self):
        return core.filters.PharmacyFilter(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filters'] = self.get_filters()
        return context

    def get_queryset(self):
        return self.get_filters().qs


class ProductInPharmacy(TitleMixin, ListView):
    title = 'Товары в наличии'
    model = core.models.Available

    def get_queryset(self):
        return core.models.Available.objects.filter(pharmacy_id=self.kwargs['pharmacy_id'])
