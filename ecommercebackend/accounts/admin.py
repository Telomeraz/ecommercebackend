from django.contrib import admin

from .models import Country, City, Address


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
        "customer",
        "full_address",
        "contact_full_name",
        "contact_phone_number",
        "city",
        "district",
        "zip_code",
    )
    search_fields = ("id", "name", "customer")
