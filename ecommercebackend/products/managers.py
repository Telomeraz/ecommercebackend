from . import models
from utils.managers import BaseManager


class ProductManager(BaseManager):
    """
    Custom manager of :model:`products.Product`.
    """

    def _create_variants(self, variants, product):
        """
        Creates variant(s) for existing product.
        """
        for variant in variants:
            variant["product"] = product
            models.ProductVariant.objects.create(variant=variant)

    def create(self, product):
        """
        Gets product (dict) and creates objects of :model:`products.Product`
        and :model:`products.ProductVariant`.
        """
        variants = product.pop("variants")
        attribute_values = product.pop("attribute_values", [])
        product = self.model(**product)
        product.save()
        product.values.add(*attribute_values)
        self._create_variants(variants=variants, product=product)
        return product


class ProductVariantManager(BaseManager):
    """
    Custom manager of :model:`products.ProductVariant`.
    """

    def create(self, variant):
        """
        Gets variant (dict) and product (object of :model:`products.Product`)
        and creates object of :model:`products.ProductVariant`.
        """
        varianter_attribute_values = variant.pop("varianter_attribute_values", [])
        variant = self.model(**variant)
        variant.save()
        variant.values.add(*varianter_attribute_values)
        return variant

    def do_archive(self, *args, **kwargs):
        """
        Archives all instances of :model:`products.ProductVariant`.
        """
        for product_variant in self.all():
            product_variant.do_archive()
