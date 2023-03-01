from django.urls import path
from . import views

urlpatterns = [
 path('', views.Catalog.as_view(), name="catalog"),
 path('about/<int:id>', views.AboutProduct.as_view(), name='aboutProduct'),
 path('comparison/', views.ProductComparison.as_view(), name='productComparison'),
 path('filters/', views.FilterProducts.as_view(), name='filters'),
 path('filter_ajax/', views.FilterProductsJson.as_view(), name='filter_ajax'),
]