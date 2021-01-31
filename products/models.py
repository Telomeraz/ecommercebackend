from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import (
    Model,
    CharField,
    TextField,
    BooleanField,
    PositiveSmallIntegerField,
    PositiveIntegerField,
    ForeignKey,
    DecimalField,
    TextChoices,
    CASCADE,
    DateTimeField,
)
from django.utils.translation import gettext_lazy as _


class Product(Model):
    """
    Stores products' common infos like name, description etc.
    """

    class Currency(TextChoices):
        USD = "USD", "$"
        EUR = "EUR", "€"
        TRY = "TRY", "₺"

    name = CharField(max_length=255, verbose_name=_("Product name"))

    subheading = CharField(
        max_length=255, blank=True, verbose_name=_("Product subheading")
    )

    description = TextField(blank=True, verbose_name=_("Product description"))

    currency = CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.TRY,
        verbose_name=_("Currency"),
    )

    tax_rate = PositiveSmallIntegerField(
        validators=(MaxValueValidator(100),),
        verbose_name=_("Price tax rate"),
    )

    is_active = BooleanField(default=True, verbose_name=_("Is product active?"))

    is_archived = BooleanField(default=False)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class ProductVariant(Model):
    """
    Stores products' non-common infos like price, stock etc.
    """

    product = ForeignKey(Product, on_delete=CASCADE, related_name="variants")

    barcode = CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name=_("Barcode"),
    )

    price = DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=(MinValueValidator(0),),
        verbose_name=_("Price"),
    )

    purchase_price = DecimalField(
        default=None,
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=12,
        validators=(MinValueValidator(0),),
        verbose_name=_("Purchase price"),
    )

    list_price = DecimalField(
        default=None,
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=12,
        validators=(MinValueValidator(0),),
        verbose_name=_("List price"),
    )

    stock = PositiveIntegerField(default=0, verbose_name=_("Stock"))

    is_primary = BooleanField(default=False, verbose_name=_("Is variant primary?"))

    is_active = BooleanField(default=True, verbose_name=_("Is variant active?"))

    is_archived = BooleanField(default=False)

    class Meta:
        verbose_name = _("Product variant")
        verbose_name_plural = _("Product variants")

    def __str__(self):
        return self.product.name
