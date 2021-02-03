from django.db import models

from . import models as product_models


class BaseManager(models.Manager):
    """
    A custom manager that filters common fields
    """

    def __init__(self, *args, **kwargs):
        self.all_objects = kwargs.pop("all_objects", False)
        super().__init__(*args, **kwargs)

    @staticmethod
    def filter_archived(queryset):
        """
        Filters queryset by is_archived field
        """
        return queryset.exclude(is_archived=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.all_objects:
            return queryset
        return self.filter_archived(queryset)


class ProductManager(BaseManager):
    """
    Custom manager of :model:`products.Product`
    """

    def create(self, product, variants):
        """
        Gets product (dict) and variants (list) and creates objects of
        :model:`products.Product` and :model:`products.ProductVariant`
        """
        product = self.model(**product)
        product.save()
        for variant in variants:
            product_models.ProductVariant.objects.create(
                variant=variant,
                product=product,
            )
        return product


class ProductVariantManager(BaseManager):
    """
    Custom manager of :model:`products.ProductVariant`
    """

    def create(self, variant, product):
        """
        Gets variant (dict) and product (object of :model:`products.Product`)
        and created object of :model:`products.ProductVariant`
        """
        variant = self.model(**variant, product=product)
        variant.save()
        return variant
