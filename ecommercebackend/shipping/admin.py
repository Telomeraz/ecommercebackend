from django.contrib import admin

from shipping.models import Courier, Package, Shipment


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`shipping.Courier`
    """

    list_display = ("id", "name")
    search_fields = ("id", "name")


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`shipping.Package`
    """

    list_display = ("id", "shipment", "created_datetime")
    search_fields = ("id", "shipment", "created_datetime")


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`shipping.Shipment`
    """

    list_display = (
        "id",
        "courier",
        "tracking_code",
        "tracking_url",
        "fee",
        "is_buyer_pays",
    )
    search_fields = (
        "id",
        "courier",
        "tracking_code",
        "tracking_url",
        "fee",
        "is_buyer_pays",
    )
