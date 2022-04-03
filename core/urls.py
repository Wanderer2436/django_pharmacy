from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='home'),
    path('catalog/', core.views.ProductList.as_view(), name='catalog'),
    path('catalog/category/<int:category_id>/', core.views.ProductList.as_view(), name='category'),
    path('catalog/product/<int:pk>/', core.views.ProductDetail.as_view(), name='products'),
    path('catalog/product/add_review/<int:pk>/', core.views.Review.as_view(), name='review'),
    path('pharmacy/', core.views.PharmacyList.as_view(), name='pharmacy'),
    path('pharmacy/<int:pharmacy_id>/', core.views.ProductInPharmacy.as_view(), name='product_in_pharmacy'),
    path('cart/', core.views.CartList.as_view(), name='cart'),
    path('cart/add_cart/<int:pk>/', core.views.add_cart, name='add_cart'),
    path('cart/delete/<int:pk>/', core.views.delete_item, name='delete_item'),
    path('cart/plus_item/<int:pk>/', core.views.plus_item, name='plus_item'),
    path('cart/minus_item/<int:pk>/', core.views.minus_item, name='minus_item'),
    path('order/', core.views.order, name='order'),
]
