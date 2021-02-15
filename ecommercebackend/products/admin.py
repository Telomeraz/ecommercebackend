from django.contrib import admin

from .models import (
    Product,
    ProductVariant,
    Attribute,
    AttributeValue,
    VarianterAttribute,
    VarianterAttributeValue,
)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.Attribute`
    """

    list_display = ("id", "name")
    search_fields = ("id", "name")


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.AttributeValue`
    """

    list_display = ("id", "name", "attribute")
    search_fields = ("id", "name", "attribute")


@admin.register(VarianterAttribute)
class VarianterAttributeAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.VarianterAttribute`
    """

    list_display = ("id", "name")
    search_fields = ("id", "name")


@admin.register(VarianterAttributeValue)
class VarianterAttributeValueAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.VarianterAttributeValue`
    """

    list_display = ("id", "name", "varianter_attribute")
    search_fields = ("id", "name", "varianter_attribute")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`products.Product`
    """

    list_display = (
        "id",
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
        "id",
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
