from django.shortcuts import render, redirect
from product.models import Product
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.views.generic import View
from product.forms import ProductForm
from seller.permissions import IsSeller
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class SellerProducts(TemplateView, APIView):
    # permission_classes = [IsSeller]

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('/login')

        if request.user.type != 'SELLER':
            return redirect('/home')

        product_form = ProductForm()
        products = Product.objects.filter(user=request.user)

        return render(
            request,
            template_name='seller/products.html',
            context={
                "all_products": products,
                "product_form": product_form,
            }
        )


class CategorizedProductView(TemplateView):

    def get(self, request, category, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('/login')

        if request.user.type != 'SELLER':
            return redirect('/home')

        product_form = ProductForm()
        products = Product.objects.filter(
            user=request.user,
            category__name__iexact=category
            )
        category_name = category

        return render(
            request,
            template_name='seller/categorized_products.html',
            context={
                "all_products": products,
                "product_form": product_form,
                "category_name": category_name,
            }
        )


class SellerProductsCreateView(TemplateView):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('/login')

        product_form = ProductForm()

        return render(
            request,
            template_name='seller/seller_products.html',
            context={
                "product_form": product_form,
            }
        )

    def post(self, request, *args, **kwargs):

        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            # #Commented logic will be used when we don't include
            # #the user field in the form
            # product = product_form.save(commit=False)
            # product.user = request.user
            # product.save()
            product_form.instance.user = request.user
            product_form.save()

            return redirect('/products')

        return render(
            request,
            template_name='seller/seller_products.html',
            context={
                "product_form": product_form,
            }
        )


class SellerProductDeleteView(DeleteView):

    model = Product
    success_url = '/products'
    template_name = 'seller/product_confirm_delete.html'


# class SellerProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductForm
#     success_url = '/products'
#     template_name = 'seller/product_update.html'
#     context_object_name = 'product_form'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#     def get_success_url(self):
#         return redirect('/products')

class SellerProductUpdateView(View):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('/login')

        product_id = kwargs['pk']
        product_details = Product.objects.get(id=product_id)

        product_form = ProductForm(instance=product_details)

        return render(
            request,
            template_name='seller/product_update.html',
            context={
                "product_form": product_form,

            })

    def post(self, request, pk, *args, **kwargs):

        product_details = Product.objects.get(id=pk)
        product_form = ProductForm(request.POST, instance=product_details)

        if product_form.is_valid():
            product_form.instance.user = request.user
            product_form.save()

            return redirect('/products')

        return render(
            request,
            template_name='seller/product_update.html',
            context={
                "product_form": product_form,

            })
