from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='home'),
    path('catalog/', core.views.ProductList.as_view(), name='catalog'),
    path('catalog/category/<int:category_id>/', core.views.ProductList.as_view(), name='category'),
    path('catalog/product/<int:pk>/', core.views.ProductDetail.as_view(), name='products'),
    path('pharmacy/', core.views.PharmacyList.as_view(), name='pharmacy'),
    path('pharmacy/<int:pharmacy_id>/', core.views.ProductInPharmacy.as_view(), name='product_in_pharmacy'),
]
