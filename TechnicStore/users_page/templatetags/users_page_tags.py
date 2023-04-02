from django import template
from catalog.models import Products

register = template.Library()


@register.filter(name='sum_price')
def sum_price(value):
    total_price = 0
    for product in value:
        this_product = Products.objects.get(id=product['product_id'])

        total_price += this_product.price * product['count']
        # total_price += product.product.price * product.count

    return total_price


@register.filter(name='mult')
def mult_price(price, count):
    print(price, count)
    return price * count


@register.filter(name='count_in_bin')
def count_in_bin(bin):
    temp = [i['count'] for i in bin]
    return sum(temp)


@register.simple_tag()
def getBasket(id):
    return Products.objects.get(id=id)
