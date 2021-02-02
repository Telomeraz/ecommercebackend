from django.contrib import admin

from .models import Product, ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.Product`
    """

    list_display = (
        "name",
        "subheading",
        "description",
        "currency",
        "tax_rate",
        "created_datetime",
        "is_active",
        "is_archived",
    )
    search_fields = ("name", "subheading", "description")


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.ProductVariant`
    """

    list_display = (
        "product",
        "barcode",
        "price",
        "purchase_price",
        "list_price",
        "stock",
        "created_datetime",
        "is_primary",
        "is_active",
        "is_archived",
    )
    search_fields = ("barcode",)
