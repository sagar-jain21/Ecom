from django.urls import path
from seller.views import (
    SellerProducts,
    SellerProductsCreateView,
    SellerProductDeleteView,
    SellerProductUpdateView,
    CategorizedSellerProductView,
    CartView,
    DeleteCartView,
    RemoveCartProductView,
)

app_name = "seller"

urlpatterns = [
    path("products/", SellerProducts.as_view(), name="seller_products"),
    path(
        "create-products/",
        SellerProductsCreateView.as_view(),
        name="create_products",
    ),
    path(
        "update-product/<uuid:pk>",
        SellerProductUpdateView.as_view(),
        name="update_product",
    ),
    path(
        "delete-product/<uuid:pk>",
        SellerProductDeleteView.as_view(),
        name="delete_product",
    ),
    path(
        "categorized-seller-products/<str:category>",
        CategorizedSellerProductView.as_view(),
        name="categorized_seller_products",
    ),
    path("add-to-cart/<uuid:id>", CartView.as_view(), name="add_to_cart"),
    path("cart/", CartView.as_view(), name="cart"),
    path("empty-cart/", DeleteCartView.as_view(), name="empty_cart"),
    path(
        "remove-product/<uuid:id>",
        RemoveCartProductView.as_view(),
        name="remove_product"
        ),
]
