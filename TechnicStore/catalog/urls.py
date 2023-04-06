from django.urls import path
from . import views

urlpatterns = [
 path('', views.Catalog.as_view(), name="catalog"),
 path('about/<int:id>', views.AboutProduct.as_view(), name='aboutProduct'),
 path('comparison/', views.ProductComparison.as_view(), name='productComparison'),
 path('filter_ajax/<str:type>', views.FilterProductsJson.as_view(), name='filter_ajax'),
 path('search/', views.SearchProductsJson.as_view(), name='search'),
 path('like/', views.Like.as_view(), name='like'),
 path('addlike/<int:id>/', views.add_liked_item, name='addLike'),
path('<str:type>', views.Catalog.as_view(), name='catalog2'),
path('comment/<int:id>', views.Comments.as_view(), name='comment'),

]
