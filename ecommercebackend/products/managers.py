from . import models
from utils.managers import BaseManager


class ProductManager(BaseManager):
    """
    Custom manager of :model:`products.Product`.
    """

    def create(self, product, variants):
        """
        Gets product (dict) and variants (list) and creates objects of
        :model:`products.Product` and :model:`products.ProductVariant`
        """
        product = self.model(**product)
        product.save()
        for variant in variants:
            models.ProductVariant.objects.create(
                variant=variant,
                product=product,
            )
        return product


class ProductVariantManager(BaseManager):
    """
    Custom manager of :model:`products.ProductVariant`.
    """

    def create(self, variant, product):
        """
        Gets variant (dict) and product (object of :model:`products.Product`)
        and created object of :model:`products.ProductVariant`.
        """
        variant = self.model(**variant, product=product)
        variant.save()
        return variant

    def do_archive(self, *args, **kwargs):
        """
        Archives all instances of :model:`products.ProductVariant`.
        """
        for product_variant in self.all():
            product_variant.do_archive()
