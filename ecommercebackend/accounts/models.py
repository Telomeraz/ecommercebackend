from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    """
    Stores country's infos.
    """

    name = models.CharField(max_length=255, unique=True, verbose_name=_("Country Name"))

    alpha2_code = models.CharField(max_length=2, unique=True, verbose_name=_("Alpha-2 Code"))

    alpha3_code = models.CharField(max_length=3, unique=True, verbose_name=_("Alpha-3 Code"))

    numeric_code = models.PositiveSmallIntegerField(
        validators=(validators.MaxValueValidator(999),),
        unique=True,
        verbose_name=_("Numeric Code"),
    )

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name


class City(models.Model):
    """
    Stores city's infos.
    """

    name = models.CharField(max_length=255, verbose_name=_("City Name"))

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return "{}, {}".format(self.name, self.country)


class Address(models.Model):
    """
    Stores address infos of user.
    """

    name = models.CharField(max_length=255, verbose_name=_("Address Name"))

    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    full_address = models.TextField(verbose_name=_("Address"))

    contact_full_name = models.CharField(max_length=255, verbose_name=_("Contact Full Name"))

    contact_phone_number = PhoneNumberField(blank=True, null=True, verbose_name=_("Contact Phone Number"))

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    district = models.CharField(max_length=255, verbose_name=_("District"))

    zip_code = models.CharField(max_length=12, verbose_name=_("Zip Code"))

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return self.name
