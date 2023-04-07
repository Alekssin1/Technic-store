from django import template
from catalog.models import Products

register = template.Library()


@register.filter(name='sum_price')
def sum_price(value):
    total_price = 0
    if value:
        id_list = [product['product_id'] for product in value]
        all_product = Products.objects.filter(id__in=id_list).only('price')
        for product, price in zip(value, all_product):
            total_price += price.price * product['count']

    return total_price


@register.filter(name='mult')
def mult_price(price, count):
    return price * count


@register.filter(name='count_in_bin')
def count_in_bin(bin):
    temp = []
    if bin:
        temp = [i['count'] for i in bin]
    return sum(temp)


@register.simple_tag()
def getBasket(id):
    return Products.objects.filter(id=id).prefetch_related('img').only(
            'title', 'price', 'img__img', 'type', 'brand', 'amount'
        ).first()
    
@register.simple_tag()
def in_basket(listt):
    basket = []
    
    for i in listt:
        basket.append(i['product_id'])
        
        
    out = Products.objects.filter(id__in=basket).prefetch_related('img')\
        .select_related('procesor').select_related('internal_memory').select_related('color')\
                .select_related('number_SIM').select_related('working_memory').select_related('screen_diagonal')\
                    .select_related('screen_type').select_related('screen_resolution').select_related('main_camera')\
                        .select_related('front_camera').select_related('battery_capacity')\
                .prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'amount', 'procesor__value', 'internal_memory__value', 
            'color__value', 'number_SIM__value', 'working_memory__value', 'screen_diagonal__value', 
            'screen_type__value', 'screen_resolution__value', 'main_camera__value', 'front_camera__value', 
            'battery_capacity__value'
        )
    
    return out

@register.filter(name='my_in')
def my_in(id, like):
    if id in [i['product_id'] for i in like]:
        return False
    return True


@register.filter(name='lens')
def lens(my_list):
    return len(my_list)