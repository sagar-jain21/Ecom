from django.shortcuts import render, redirect
from product.models import Product
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.views.generic import View
from product.forms import ProductForm
from buyer.models import Cart


class SellerProducts(TemplateView):
    # permission_classes = [IsSeller]

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('/login')

        if request.user.groups.filter(name='seller').exists():
            products = Product.objects.filter(user=request.user)
        else:
            products = Product.objects.all()

        product_form = ProductForm()

        return render(
            request,
            template_name='seller/products.html',
            context={
                "all_products": products,
                "product_form": product_form,
            }
        )


class CategorizedSellerProductView(TemplateView):

    def get(self, request, category, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('/login')

        if request.user.groups.filter(name='seller').exists():
            products = Product.objects.filter(
                user=request.user,
                category__name__iexact=category
            )
        else:
            products = Product.objects.filter(category__name__iexact=category)

        product_form = ProductForm()
        category_name = category

        return render(
            request,
            template_name='seller/categorized_seller_products.html',
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

        if request.user.groups.filter(name='seller').exists():
            product_form = ProductForm()

            return render(
                request,
                template_name='seller/seller_products.html',
                context={
                    "product_form": product_form,
                }
            )
        else:
            return redirect('/home')

    def post(self, request, *args, **kwargs):

        if not request.user.groups.filter(name='seller').exists():
            return redirect('/home')

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

        if not request.user.groups.filter(name='seller').exists():
            return redirect('/home')

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

        if not request.user.groups.filter(name='seller').exists():
            return redirect('/home')

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


class CartView(TemplateView):
    def post(self, request, id, *args, **kwargs):

        if not request.user.groups.filter(name='buyer').exists():
            return redirect('/home')

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.products.add(id)

        return redirect('/home')

    def get(self, request, *args, **kwargs):
        # cart_products = Cart.objects.filter(user=request.user).values_list(
        #     "products__id", "products__name"
        # )
        # cart = Cart.objects.get(user=request.user).products.all()

        if not request.user.groups.filter(name='buyer').exists():
            return redirect('/home')

        cart = Cart.objects.prefetch_related("products").filter(user=request.user).first()
        if cart:
            cart_products = cart.products.all()
        else:
            cart_products = None

        return render(
            request,
            template_name="seller/cart.html",
            context={
                "cart_products": cart_products,
            },
        )


class RemoveCartProductView(View):

    def get(self, request, id, *args, **kwargs):

        if not request.user.groups.filter(name='buyer').exists():
            return redirect('/home')

        product = Product.objects.filter(id=id).first()

        cart = Cart.objects.filter(products=product).first()

        cart.products.remove(id)

        return redirect('/cart')


class DeleteCartView(View):

    def post(self, request, *args, **kwargs):

        if not request.user.groups.filter(name='buyer').exists():
            return redirect('/home')

        cart = Cart.objects.get(user=request.user)
        cart.delete()

        return redirect("/cart")
