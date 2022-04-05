from django.urls import path
import basket.views

app_name = 'basket'

urlpatterns = [
    path('', basket.views.basket_detail, name='basket_detail'),
    path('add/<int:product_id>/', basket.views.basket_add, name='basket_add'),
    path('remove/<int:product_id>/', basket.views.basket_remove, name='basket_delete'),
    path('plus_item/<int:product_id>/', basket.views.plus_item, name='plus_item'),
    path('minus_item/<int:product_id>/', basket.views.minus_item, name='minus_item'),
    path('create/', basket.views.order_create, name='order_create'),
    path('complete/', basket.views.order_complete, name='order_complete'),
]
