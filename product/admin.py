from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "price"
    ]

# admin.site.register(Product)
