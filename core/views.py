from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
import core.models
import core.filters
from django.urls import reverse
import core.forms


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
        context['review'] = core.models.Review.objects.all()
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['review'] = core.models.Review.objects.all()
        return context


class Review(TitleMixin, CreateView):
    model = core.models.Review
    title = 'Добавление отзыва'
    template_name = 'core/review.html'
    fields = ['review']
    product = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.product = form.instance.product = core.models.Product.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('core:products', kwargs={'pk': self.kwargs['pk']})


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


class ProductUpdate(TitleMixin, UpdateView):
    model = core.models.Product
    form_class = core.forms.ProductEdit

    def get_title(self):
        return f'Изменение данных товара "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('core:catalog')


class ProductCreate(TitleMixin, CreateView):
    model = core.models.Product
    form_class = core.forms.ProductEdit
    title = 'Добавление товара'

    def get_success_url(self):
        return reverse('core:catalog')


class ProductDelete(TitleMixin, DeleteView):
    model = core.models.Product

    def get_title(self):
        return f'Удаление товара {str(self.get_object())}'

    def get_success_url(self):
        return reverse('core:catalog')




