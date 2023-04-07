from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


from .utils import CatalogMixin
from catalog.models import Products, ProductsBrand, ValueProductAttributes, Comment, CommentContent
from .form import CommentForm


class AboutProduct(CatalogMixin, DetailView):

    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        context = self.renderPage()
        context['product'] = Products.objects.filter(id=self.kwargs.get("id"))\
            .select_related('procesor').select_related('internal_memory').select_related('color')\
                .select_related('number_SIM').select_related('working_memory').select_related('screen_diagonal')\
                    .select_related('screen_type').select_related('screen_resolution').select_related('main_camera')\
                        .select_related('front_camera').select_related('battery_capacity')\
                .prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'amount', 'procesor__value', 'internal_memory__value', 'color__value',
            'number_SIM__value', 'working_memory__value', 'screen_diagonal__value', 'screen_type__value', 'screen_resolution__value',
            'main_camera__value', 'front_camera__value', 'battery_capacity__value'
        ).first()
        context['like'] = self.request.session['like']
        return render(request, 'catalog/aboutProduct.html', context=context)


class ProductComparison(CatalogMixin, ListView):

    def get(self, request):
        context = self.renderPage()
        context['comparison'] = self.request.session['comparison']
        return render(request, "catalog/productComparison.html", context=context)


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
        
        context['like'] = self.request.session['like']

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


class Catalog(CatalogMixin, DetailView):
    def get(self, request, *args, **kwargs):
        type = self.kwargs.get("type")
        context = self.renderPage()
        context['products'] = Products.objects.all().filter(type__type=type).select_related('brand')\
        .prefetch_related('img').prefetch_related('type__characteristic')\
            .prefetch_related('type__characteristic__value').only(
            'title', 'price', 'img', 'type', 'brand', 'amount', 
            'type__characteristic__attribute', 'type__characteristic__value__value'
        )

        brands_all = [i.brand.brand for i in context['products']]
        brands = list(set(brands_all))

        context['brands'] = brands
        context['sort'] = "за популярністю"
        context['type'] = type
        context['like'] = self.request.session['like']
        return render(request, 'catalog/catalog.html', context=context)


class Comments(CatalogMixin, DetailView, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        context = self.renderPage()
        context['product'] = Products.objects.filter(id=self.kwargs.get("id")).prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'amount',
        ).first()
        context['form'] = CommentForm()

        context['comments'] = get_object_or_404(
            Products, id=self.kwargs.get("id"))

        return render(request, 'catalog/comment.html', context=context)

    def add_comment(self, rating, text):
        comment_content = CommentContent()
        comment_content.text = text
        comment_content.rating = rating
        comment_content.author_name = self.request.user.username
        comment_content.save()
        return comment_content

    def post(self, request, *args, **kwargs):
        rating = request.POST.get('rating')
        text = request.POST.get('text')

        product = get_object_or_404(Products, id=self.kwargs.get("id"))

        if not product.comments:
            my_comment = Comment.objects.create(count=1, average_score=rating)
            comment_content = self.add_comment(rating, text)
            my_comment.content.add(comment_content)
            my_comment.save()

            product.comments = my_comment
            product.save()
        else:
            if self.request.user.username in [i.author_name for i in product.comments.content.all()]:
                context = self.renderPage()
                context['comments'] = product
                self.errors = []
                self.errors.append('Ви вже залишали відгук про цей товар')
                context['errors'] = self.errors
                return render(request, 'catalog/partials/comment_content.html', context=context)
            comment_content = self.add_comment(rating, text)
            product.comments.content.add(comment_content)
            comment_count = product.comments.content.count()
            
            if product.comments.average_score:
                new_average_score = (
                    (comment_count-1) * product.comments.average_score + float(rating))/comment_count
            else:
                new_average_score = rating

            product.comments.count = comment_count
            product.comments.average_score = new_average_score
            product.save()

        context = self.renderPage()
        context['comments'] = product

        return render(request, 'catalog/partials/comment_content.html', context=context)


class Like(CatalogMixin, ListView): 
    
    def get(self, request, *args, **kwargs):
        context = self.renderPage()
        context['like'] = self.request.session['like']
        return render(request, 'catalog/like.html', context=context)


def add_liked_item(request, id):
    if request.session.get('like'):
        liked_items = request.session['like']
        product_ids = [item['product_id'] for item in liked_items]
        if id in product_ids:
            for index, item in enumerate(liked_items):
                if item['product_id'] == id:
                    del liked_items[index]
                    break
        else:
            liked_items.append({'product_id': id})
    else:
        request.session['like'] = [{'product_id': id}]
    
    request.session.modified = True
    return render(request, 'catalog/partials/empty_page.html', context={'like': request.session['like']})

def add_comparison_item(request, id):
    if request.session.get('comparison'):
        comparison_items = request.session['comparison']
        product = Products.objects.get(id=id)
        if str(product.type) == comparison_items[0]['type']: #same type
            product_ids = [item['product_id'] for item in comparison_items]
            if id in product_ids:
                for index, item in enumerate(comparison_items):
                    if item['product_id'] == id:
                        del comparison_items[index]
                        break
            else:
                comparison_items.append({'product_id': id, 'type': str(product.type)})
    else:
        product = Products.objects.get(id=id)
        request.session['comparison'] = [{'product_id': id, 'type': str(product.type)}]
    
    print(request.session['comparison'])
    request.session.modified = True
    return render(request, 'catalog/partials/empty_page.html', context={'comparison': request.session['comparison']})