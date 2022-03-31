from django.db.models import Count, Sum, Max
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
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


class CartList(TitleMixin, ListView):
    title = 'Корзина'
    model = core.models.CartItem
    template_name = 'core/cart_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['total_sum'] = core.models.CartItem.objects.all().aggregate(Sum('total_price'))['total_price__sum']
        return context


def add_cart(request, pk):
    cart = core.models.Cart.objects.get_or_create(user=request.user)[0]
    print(request.user.pk)
    product = get_object_or_404(core.models.Product, pk=pk)
    cartitem = core.models.CartItem.objects.get_or_create(cart_id=cart.pk, product=product, price=product.price)
    return redirect('/cart/')


def delete_item(request, pk):
    record = core.models.CartItem.objects.get(pk=pk)
    record.delete()
    return redirect('/cart/')


def plus_item(request, pk):
    item = core.models.CartItem.objects.get(pk=pk)
    item.quantity += 1
    item.save()
    return redirect('/cart/')


def minus_item(request, pk):
    item = core.models.CartItem.objects.get(pk=pk)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('/cart/')


def order(request):
    record = core.models.CartItem.objects.all()
    record.delete()
    return redirect('core:home')