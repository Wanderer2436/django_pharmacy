from django.shortcuts import render, redirect, get_object_or_404
from core.models import Product
from .basket import Basket
from basket.forms import OrderCreateForm
from basket.models import OrderItem, Order


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/basket_detail.html', {'basket': basket})


def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.add(product=product)
    return redirect('basket:basket_detail')


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.remove(product)
    return redirect('basket:basket_detail')


def plus_item(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.plus(product=product)
    return redirect('basket:basket_detail')


def minus_item(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.minus(product=product)
    return redirect('basket:basket_detail')


def order_create(request):
    basket = Basket(request)
    order = Order.objects.create(user=request.user)
    for item in basket:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    basket.clear()
    return render(request, 'basket/create.html', {'basket': basket, 'order': order})


def order_complete(request):
    return render(request, 'basket/created.html')
