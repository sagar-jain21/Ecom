from django.urls import path
from seller.views import (
    SellerProducts,
    SellerProductsCreateView,
    SellerProductDeleteView,
    SellerProductUpdateView,
    CategorizedProductView,
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
        "categorized-products/<str:category>",
        CategorizedProductView.as_view(),
        name="categorized_products",
    ),
]
