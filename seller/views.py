from django.shortcuts import render
from product.models import Product
from django.views.generic.base import TemplateView
from product.forms import ProductForm


class SellerProducts(TemplateView):

    def get(self, request, *args, **kwargs):

        products = Product.objects.all()

        return render(
            request,
            template_name='seller/products.html',
            context={
                "all_products": products,
            }
        )
