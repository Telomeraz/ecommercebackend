"""
Contains admin pages of models in :module:`products.models`
"""

from django.contrib import admin

from .models import Product, ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.Product`
    """

    search_fields = ("name", "subheading", "description")


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.ProductVariant`
    """

    search_fields = ("barcode",)
