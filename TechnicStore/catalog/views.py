from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponse

from .utils import CatalogMixin
from .models import Products, ProductsBrand, ValueProductAttributes
from django.urls import reverse


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


class FilterProductsJson(CatalogMixin, DetailView):

    def get_query(self, attribute_in_db, attribute_name, all_attributes):
        if not self.request.GET.get(attribute_name, False):
            return Q(**{f"{attribute_in_db}__value__in": all_attributes})
        else:
            return Q(**{f"{attribute_in_db}__value__in": self.request.GET.getlist(attribute_name)})

    def get_queryset(self):
        type = self.kwargs.get("type")
        all_brands = [i.brand for i in ProductsBrand.objects.all()]
        all_ValueProductAttributes = [
            i.value for i in ValueProductAttributes.objects.all()]

        if not self.request.GET.get("brand", False):
            brand = Q(brand__brand__in=all_brands)
        else:
            brand = Q(brand__brand__in=self.request.GET.getlist('brand'))

        procesor = self.get_query(
            'procesor', "Процесор", all_ValueProductAttributes)
        internal_memory = self.get_query(
            'internal_memory', "Внутрішня пам'ять", all_ValueProductAttributes)
        color = self.get_query('color', "Колір", all_ValueProductAttributes)
        number_SIM = self.get_query(
            'number_SIM', "Кількість SIM-карт", all_ValueProductAttributes)
        working_memory = self.get_query(
            'working_memory', "Оперативна пам'ять", all_ValueProductAttributes)
        screen_diagonal = self.get_query(
            'screen_diagonal', "Діагональ екрану", all_ValueProductAttributes)
        screen_type = self.get_query(
            'screen_type', "Тип екрану", all_ValueProductAttributes)
        screen_resolution = self.get_query(
            'screen_resolution', "Роздільна здатність екрану", all_ValueProductAttributes)
        main_camera = self.get_query(
            'main_camera', "Основна камера", all_ValueProductAttributes)
        front_camera = self.get_query(
            'front_camera', "Фронтальна камера", all_ValueProductAttributes)
        battery_capacity = self.get_query(
            'battery_capacity', "Ємність аккумулятора", all_ValueProductAttributes)

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
            Q(type__type=type)
            & brand
            & Q(price__gte=self.request.GET.get('price_start'), price__lte=self.request.GET.get('price_end'))
            & procesor
            & internal_memory
            & color
            & number_SIM
            & working_memory
            & screen_diagonal
            & screen_type
            & screen_resolution
            & main_camera
            & front_camera
            & battery_capacity
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

        context = {'products': queryset,
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


class Catalog2(CatalogMixin, DetailView):
    def get(self, request, *args, **kwargs):
        type = self.kwargs.get("type")
        context = self.renderPage()
        context['products'] = Products.objects.all().filter(type__type=type).prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'amount',
        )

        brands_all = [i.brand.brand for i in context['products']]
        brands = list(set(brands_all))

        context['brands'] = brands
        context['sort'] = "за популярністю"
        context['type'] = type
        if context.get('products', False):
            context['filters'] = context['products'][0].type.characteristic.all()
        return render(request, 'catalog/catalog.html', context=context)
