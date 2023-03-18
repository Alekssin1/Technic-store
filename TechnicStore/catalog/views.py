from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponse

from .utils import CatalogMixin
from .models import Products, ProductsBrand

    
class Catalog(CatalogMixin, ListView):
    
    def get(self, request):
        context = self.renderPage()
        context['products'] = Products.objects.all().prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'amount',
        )
        context['brands'] = ProductsBrand.objects.all()
        context['sort'] = "за популярністю"
        return render(request, 'catalog/catalog.html', context=context)


class AboutProduct(CatalogMixin, DetailView):
    
    pk_url_kwarg = 'id'
    
    def get(self, request, *args, **kwargs):
        context = self.renderPage()
        context['product'] = Products.objects.filter(id=self.kwargs.get("id")).prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'amount',
        ).first()
        return render(request, 'catalog/aboutProduct.html', context=context)

         
class ProductComparison(ListView):
    
    def get(self, request):
         return HttpResponse("ProductComparison")

class FilterProducts(ListView):
    
    def get(self, request):
         return HttpResponse("FilterProducts")
    
class FilterProductsJson(ListView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("FilterProductsJson")