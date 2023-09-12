from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from product.forms import ProductForm
from product.models import Product
from buyer.models import Cart
from django.views import View


class AllProductsView(TemplateView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")

        product_form = ProductForm()
        all_products = Product.objects.all()

        return render(
            request,
            template_name="buyer/all_products.html",
            context={
                "all_products": all_products,
                "product_form": product_form,
            },
        )


class CategorizedProductsView(TemplateView):
    def get(self, request, category, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")

        if request.user.type != "BUYER":
            return redirect("/home")

        product_form = ProductForm()
        products = Product.objects.filter(category__name__iexact=category)
        category_name = category

        return render(
            request,
            template_name="buyer/categorized_products.html",
            context={
                "all_products": products,
                "product_form": product_form,
                "category_name": category_name,
            },
        )


class CartView(TemplateView):
    def post(self, request, id, *args, **kwargs):

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.products.add(id)

        return redirect('/home')

    def get(self, request, *args, **kwargs):
        # cart_products = Cart.objects.filter(user=request.user).values_list(
        #     "products__id", "products__name"
        # )
        # cart = Cart.objects.get(user=request.user).products.all()

        cart = Cart.objects.prefetch_related("products").filter(user=request.user).first()
        if cart:
            cart_products = cart.products.all()
        else:
            cart_products = None

        return render(
            request,
            template_name="buyer/cart.html",
            context={
                "cart_products": cart_products,
            },
        )


class RemoveCartProductView(View):

    def get(self, request, id, *args, **kwargs):

        product = Product.objects.filter(id=id).first()

        cart = Cart.objects.filter(products=product).first()

        cart.products.remove(id)

        return redirect('/cart')


class DeleteCartView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart.delete()

        return redirect("/cart")
