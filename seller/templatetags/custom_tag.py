from django import template
from product.models import Product
register = template.Library()


@register.simple_tag
def count_of_products():
    return Product.objects.count()
