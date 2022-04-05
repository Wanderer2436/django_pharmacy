from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='home'),
    path('catalog/', core.views.ProductList.as_view(), name='catalog'),
    path('catalog/category/<int:category_id>/', core.views.ProductList.as_view(), name='category'),
    path('catalog/create', core.views.ProductCreate.as_view(), name='product_create'),
    path('catalog/product/<int:pk>/delete/', core.views.ProductDelete.as_view(), name='product_delete'),
    path('catalog/product/<int:pk>/update/', core.views.ProductUpdate.as_view(), name='product_update'),
    path('catalog/product/<int:pk>/', core.views.ProductDetail.as_view(), name='products'),
    path('catalog/product/add_review/<int:pk>/', core.views.Review.as_view(), name='review'),
    path('pharmacy/', core.views.PharmacyList.as_view(), name='pharmacy'),
    path('pharmacy/<int:pharmacy_id>/', core.views.ProductInPharmacy.as_view(), name='product_in_pharmacy'),
]
