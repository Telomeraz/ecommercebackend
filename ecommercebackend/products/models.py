from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers


class Product(models.Model):
    """
    Stores product's common infos like name, description etc.
    """

    class Currency(models.TextChoices):
        """
        Contains currency choices for prices.
        """

        USD = "USD", "$"
        EUR = "EUR", "€"
        TRY = "TRY", "₺"

    name = models.CharField(max_length=255, verbose_name=_("Product name"))

    subheading = models.CharField(max_length=255, blank=True, verbose_name=_("Product subheading"))

    description = models.TextField(blank=True, verbose_name=_("Product description"))

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.TRY,
        verbose_name=_("Currency"),
    )

    tax_rate = models.PositiveSmallIntegerField(
        validators=(validators.MaxValueValidator(100),),
        verbose_name=_("Price tax rate"),
    )

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date and Time"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is product active?"))

    is_archived = models.BooleanField(
        default=False,
        help_text="This is a flag that represents whether deleted. True means deleted.",
    )

    objects = managers.ProductManager()
    all_objects = managers.ProductManager(all_objects=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def do_archive(self):
        """
        Archives instance of the model and its variants.
        """
        self.is_archived = True
        self.save()
        product_variants = self.variants
        product_variants.do_archive()


class ProductVariant(models.Model):
    """
    Stores product's non-common infos like price, stock etc.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")

    barcode = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Barcode"),
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=(validators.MinValueValidator(0),),
        verbose_name=_("Price"),
    )

    purchase_price = models.DecimalField(
        default=None,
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=12,
        validators=(validators.MinValueValidator(0),),
        verbose_name=_("Purchase price"),
    )

    list_price = models.DecimalField(
        default=None,
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=12,
        validators=(validators.MinValueValidator(0),),
        verbose_name=_("List price"),
    )

    stock = models.PositiveIntegerField(default=0, verbose_name=_("Stock"))

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date and Time"))

    is_primary = models.BooleanField(default=False, verbose_name=_("Is variant primary?"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is variant active?"))

    is_archived = models.BooleanField(
        default=False,
        help_text="This is a flag that represents whether deleted. True means deleted.",
    )

    objects = managers.ProductVariantManager()
    all_objects = managers.ProductVariantManager(all_objects=True)

    class Meta:
        verbose_name = _("Product variant")
        verbose_name_plural = _("Product variants")

    def __str__(self):
        return self.product.name

    def do_archive(self):
        """
        Archives instance of the model.
        """
        self.is_archived = True
        self.save()
