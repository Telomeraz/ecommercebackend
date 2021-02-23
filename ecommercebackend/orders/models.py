from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product
from utils.models import Currency


class Package(models.Model):
    """
    Stands for packaging order lines. You can package one or more order lines
    by using this model for shipment processes.
    """

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date and time"))

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return "Packaged at {}".format(self.created_datetime)


class Order(models.Model):
    """
    Stores order's infos like addresses, customer etc.
    """

    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")

    shipping_address = models.JSONField(verbose_name=_("Shipping address"))

    billing_address = models.JSONField(verbose_name=_("Billing address"))

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date and time"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return "{}'s order. ID: {}".format(self.customer.email, self.id)

    @property
    def total(self):
        total_price = 0
        for order_line in self.lines.all():
            total_price += order_line.total_price

        return total_price


class OrderLine(models.Model):
    """
    Stores line's infos of order.
    """

    class Status(models.TextChoices):
        """
        Contains status choices for order line.
        """

        RECEIVED = "RECEIVED", _("Received")
        APPROVED = "APPROVED", _("Approved")
        DECLINED = "DECLINED", _("Declined")
        PACKAGED = "PACKAGED", _("Packaged")
        CANCELLED = "CANCELLED", _("Cancelled")
        SHIPPED = "SHIPPED", _("Shipped")
        DELIVERED = "DELIVERED", _("Delivered")
        UNDELIVERED = "UNDELIVERED", _("Undelivered")
        REFUNDED = "REFUNDED", _("Refunded")
        COMPLETED = "COMPLETED", _("Completed")

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="lines")

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="order_lines",
    )

    package = models.ForeignKey(
        Package,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="order_lines",
        help_text=_("Seller can package and send packaged order lines together for shipment."),
    )

    status = models.CharField(
        max_length=55,
        choices=Status.choices,
        default=Status.RECEIVED,
        verbose_name=_("Status"),
    )

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        verbose_name=_("Currency"),
    )

    tax_rate = models.PositiveSmallIntegerField(
        validators=(validators.MaxValueValidator(100),),
        verbose_name=_("Price tax rate"),
    )

    unit_price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=(validators.MinValueValidator(0),),
        verbose_name=_("Unit price"),
        help_text=_("Unit price including discount and tax"),
    )

    quantity = models.PositiveIntegerField(
        validators=(validators.MinValueValidator(1),),
        verbose_name=_("Quantity"),
    )

    discount_rate = models.PositiveSmallIntegerField(
        validators=(validators.MaxValueValidator(100),),
        blank=True,
        default=0,
        verbose_name=_("Discount rate"),
    )

    class Meta:
        verbose_name = _("Order Line")
        verbose_name_plural = _("Order Lines")

    def __str__(self):
        return self.product.name

    @property
    def unit_price_excluding_discount(self):
        unit_price_excluding_discount = (self.unit_price * 100) / (100 - self.discount_rate)
        return round(unit_price_excluding_discount, 2)

    @property
    def unit_price_excluding_tax(self):
        unit_price_excluding_tax = self.unit_price_excluding_discount * (100 - self.tax_rate)
        return round(unit_price_excluding_tax, 2)

    @property
    def total_price(self):
        return self.unit_price * self.quantity
