from django.urls import path
from seller.views import (
    SellerProducts,
    SellerProductsCreateView,
    SellerProductDeleteView,
    SellerProductUpdateView,
    )

app_name = "seller"

urlpatterns = [
    path("products/", SellerProducts.as_view(), name="seller_products"),
    path(
        "createproducts/",
        SellerProductsCreateView.as_view(),
        name="create_products",
    ),
    path(
        "updateproduct/<uuid:pk>",
        SellerProductUpdateView.as_view(),
        name="update_product"
        ),
    path(
        "deleteproduct/<uuid:pk>",
        SellerProductDeleteView.as_view(),
        name="delete_product"
        ),
]
