from django import template
from catalog.models import Products

register = template.Library()


@register.filter(name='sum_price')
def sum_price(value):
    total_price = 0
    if value:
        for product in value:
            this_product = Products.objects.get(id=product['product_id'])
            total_price += this_product.price * product['count']

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
    return Products.objects.get(id=id)


@register.filter(name='my_in')
def my_in(id, like):
    if id in [i['product_id'] for i in like]:
        return False
    return True


@register.filter(name='lens')
def lens(my_list):
    return len(my_list)