from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts import managers
from utils.models import AbstractArchive, OwnerMixin


class User(AbstractUser):
    pass


class Country(models.Model):
    """
    Stores country's infos.
    """

    name = models.CharField(max_length=255, unique=True, verbose_name=_("Country name"))

    alpha2_code = models.CharField(max_length=2, unique=True, verbose_name=_("Alpha-2 code"))

    alpha3_code = models.CharField(max_length=3, unique=True, verbose_name=_("Alpha-3 code"))

    numeric_code = models.PositiveSmallIntegerField(
        validators=(validators.MaxValueValidator(999),),
        unique=True,
        verbose_name=_("Numeric code"),
    )

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ("name",)

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
        ordering = ("name",)

    def __str__(self):
        return "{}, {}".format(self.name, self.country)


class Address(AbstractArchive, OwnerMixin):
    """
    Stores address infos of user.
    """

    name = models.CharField(max_length=255, verbose_name=_("Address name"))

    full_address = models.TextField(verbose_name=_("Address"))

    contact_full_name = models.CharField(max_length=255, verbose_name=_("Contact full name"))

    contact_phone_number = PhoneNumberField(blank=True, verbose_name=_("Contact phone number"))

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    district = models.CharField(max_length=255, verbose_name=_("District"))

    zip_code = models.CharField(max_length=12, verbose_name=_("Zip code"))

    objects = managers.AddressManager()
    all_objects = managers.AddressManager(all_objects=True)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return self.name


class Customer(AbstractArchive):
    """
    Stores customer infos. This model is used for non-user orders. If an order
    is third-party software order or manuel order which is created by admin,
    this model should be used for customer infos of those type of orders.
    """

    first_name = models.CharField(max_length=255, blank=True, verbose_name=_("First name"))

    last_name = models.CharField(max_length=255, blank=True, verbose_name=_("Last name"))

    email = models.EmailField(_("Email address"), blank=True)

    phone_number = PhoneNumberField(blank=True, verbose_name=_("Contact phone number"))

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
