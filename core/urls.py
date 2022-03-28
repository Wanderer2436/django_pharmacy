from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='home'),
    path('catalog/', core.views.ProductList.as_view(), name='catalog'),
    path('catalog/category/<int:category_id>/', core.views.ProductList.as_view(), name='category'),
    path('catalog/product/<int:pk>/', core.views.ProductDetail.as_view(), name='products'),
]
