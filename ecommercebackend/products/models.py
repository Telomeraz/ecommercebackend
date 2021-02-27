from django.contrib.contenttypes.fields import GenericRelation
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers
from images.models import Image
from utils.models import ArchiveMixin, Currency


class BaseAttribute(models.Model):
    """
    Base abstract model for attributes and its values.
    """

    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Attribute(BaseAttribute):
    """
    Stores non-varianter attributes.
    """

    pass


class AttributeValue(BaseAttribute):
    """
    Stores non-varianter attribute values.
    """

    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name="values",
    )


class VarianterAttribute(BaseAttribute):
    """
    Stores varianter attributes.
    """

    pass


class VarianterAttributeValue(BaseAttribute):
    """
    Stores non-varianter attribute values.
    """

    varianter_attribute = models.ForeignKey(
        VarianterAttribute,
        on_delete=models.CASCADE,
        related_name="varianter_values",
    )


class Product(ArchiveMixin):
    """
    Stores product's common infos like name, description etc.
    """

    name = models.CharField(max_length=255, verbose_name=_("Product name"))

    subheading = models.CharField(max_length=255, blank=True, verbose_name=_("Product subheading"))

    description = models.TextField(blank=True, verbose_name=_("Product description"))

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        verbose_name=_("Currency"),
    )

    tax_rate = models.PositiveSmallIntegerField(
        validators=(validators.MaxValueValidator(100),),
        verbose_name=_("Price tax rate"),
    )

    values = models.ManyToManyField(AttributeValue, blank=True, related_name="products")

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date and time"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is product active?"))

    objects = managers.ProductManager()
    all_objects = managers.ProductManager(all_objects=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def update(self, data):
        attribute_values = data.pop("attribute_values", [])
        for key, value in data.items():
            setattr(self, key, value)
        self.save()
        self.values.add(*attribute_values)

    def do_archive(self):
        """
        Archives instance of the model and its variants.
        """
        super().do_archive()
        product_variants = self.variants
        product_variants.do_archive()


class ProductVariant(ArchiveMixin):
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

    values = models.ManyToManyField(VarianterAttributeValue, blank=True, related_name="product_variants")

    images = GenericRelation(Image, related_query_name="product_variants")

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date and time"))

    is_primary = models.BooleanField(default=False, verbose_name=_("Is variant primary?"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is variant active?"))

    objects = managers.ProductVariantManager()
    all_objects = managers.ProductVariantManager(all_objects=True)

    class Meta:
        verbose_name = _("Product variant")
        verbose_name_plural = _("Product variants")

    def __str__(self):
        return self.product.name
