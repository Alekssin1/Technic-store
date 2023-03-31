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

    
class FilterProductsJson(CatalogMixin, ListView):
    def get_queryset(self):
        all_brands = [i.brand for i in ProductsBrand.objects.all()]
        if not self.request.GET.get("brand", False):
            brand =  Q(brand__brand__in=all_brands)
        else:
            brand = Q(brand__brand__in=self.request.GET.getlist('brand'))
      
        if self.request.GET.getlist('price_up'):
            sort = 'price'
            sort_text = 'за зростанням ціни'
        elif self.request.GET.getlist('price_down'):
            sort = '-price'
            sort_text = 'за зменшенням ціни'
        else:
            sort = 'id'
            sort_text = 'за популярністю'
            
        query = Products.objects.filter(
            brand &
            Q(price__gte=self.request.GET.get('price_start'), price__lte=self.request.GET.get('price_end'))
            ).prefetch_related('img').values('title', 'price', 'img__img', 'id').distinct().order_by(sort)
    
        return query, sort_text

    def get(self, request, *args, **kwargs):
        queryset, sort_text = self.get_queryset()
        temp = []
        temp.clear()

        queryset = list(queryset)
        my_len = len(queryset)    
        i = 0
        while i < my_len:
            if queryset[i]['title'] not in temp:
                temp.append(queryset[i]['title'])
                i += 1
            else:
                del queryset[i]
                my_len -= 1
                
        context= {'products': queryset,
                  'sort': sort_text}
       
        return render(request, 'catalog/partials/catalog__product.html', context=context)
    
class SearchProductsJson(CatalogMixin, ListView):
    def post(self, request, *args, **kwargs):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            res = None
            product = self.request.POST.get('product')
            qs = Products.objects.filter(
                Q(title__icontains=product) | Q(brand__brand__icontains=product))
            if len(qs) > 0 and len(product) > 0:
                data = []
                for pos in qs:
                    item = {
                        'id': pos.pk,
                        'title': pos.title,
                        'price': pos.price,
                        'image': pos.img.all()[0].img.url
                    }
                    data.append(item)
                res = data
            else:
                res = "По вашому запиту нічого не знайдено"
            return JsonResponse({'data': res})
        return JsonResponse({})
