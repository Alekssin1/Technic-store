from django import template

register = template.Library()

@register.filter(name='sum_price')
def sum_price(value):
    total_price = 0
    for product in value:
        total_price += product.product.price * product.count
        
    return total_price

@register.filter(name='mult')
def mult_price(price, count):
    return price * count

@register.filter(name='count_in_bin')
def count_in_bin(bin):
    temp = [i.count for i in bin.all()]
    return sum(temp) 