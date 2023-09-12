# from django.urls import path
# from buyer.views import (
#     AllProductsView,
#     CategorizedProductsView,
#     CartView,
#     DeleteCartView,
#     RemoveCartProductView,
# )

# app_name = "buyer"

# urlpatterns = [
#     path("all-products/", AllProductsView.as_view(), name="all_products"),  # Done
#     path(
#         "categorized-products/<str:category>",  #done
#         CategorizedProductsView.as_view(),
#         name="categorized_products",
#     ),
#     path("add-to-cart/<uuid:id>", CartView.as_view(), name="add_to_cart"),
#     path("cart/", CartView.as_view(), name="cart"),
#     path("empty-cart/", DeleteCartView.as_view(), name="empty_cart"),
#     path(
#         "remove-product/<uuid:id>",
#         RemoveCartProductView.as_view(),
#         name="remove_product"
#         ),
# ]
