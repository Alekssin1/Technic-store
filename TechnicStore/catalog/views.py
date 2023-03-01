from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

    
class Catalog(ListView):
    
    def get(self, request):
         return HttpResponse("Catalog")


class AboutProduct(DetailView):
    
    pk_url_kwarg = 'id'
    
    def get(self, request, *args, **kwargs):
         return HttpResponse("AboutProduct")

         
class ProductComparison(ListView):
    
    def get(self, request):
         return HttpResponse("ProductComparison")

class FilterProducts(ListView):
    
    def get(self, request):
         return HttpResponse("FilterProducts")
    
class FilterProductsJson(ListView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("FilterProductsJson")