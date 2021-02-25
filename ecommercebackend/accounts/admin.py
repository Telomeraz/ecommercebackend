from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Country, City, Address, User


admin.site.register(User, UserAdmin)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`accounts.Country`
    """

    list_display = ("id", "name", "alpha2_code", "alpha3_code", "numeric_code")
    search_fields = ("id", "name", "alpha2_code", "alpha3_code", "numeric_code")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`accounts.City`
    """

    list_display = ("id", "name")
    search_fields = ("id", "name")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`accounts.Address`
    """

    list_display = (
        "id",
        "name",
        "owner_content_type",
        "owner_object_id",
        "owner",
        "full_address",
        "contact_full_name",
        "contact_phone_number",
        "city",
        "district",
        "zip_code",
    )
    search_fields = ("id", "name", "customer")
