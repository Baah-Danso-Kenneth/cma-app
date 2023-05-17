from ..models import Order, Customer, Product
from django import template

register = template.Library()


@register.simple_tag
def related_products(id):
    customer = Customer.objects.get(id=id)
    products = customer.order_customer.all()
    return products
