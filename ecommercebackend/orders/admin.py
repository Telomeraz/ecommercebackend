from django.contrib import admin

from .models import Order, OrderLine


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`orders.Order`
    """

    list_display = (
        "id",
        "customer",
        "shipping_address",
        "billing_address",
        "total",
        "created_datetime",
    )
    search_fields = ("id",)


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`orders.OrderLine`
    """

    list_display = (
        "id",
        "order",
        "product",
        "package",
        "status",
        "currency",
        "tax_rate",
        "unit_price",
        "quantity",
        "discount_rate",
        "unit_price_excluding_discount",
        "unit_price_excluding_tax",
        "total_price",
    )
    search_fields = ("id", "status")
