from django import template
from product.models import Product
from django.contrib.auth.models import Group
register = template.Library()


@register.simple_tag
def count_of_products():
    return Product.objects.count()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.filter(name=group_name).first()
    return True if group in user.groups.all() else False
