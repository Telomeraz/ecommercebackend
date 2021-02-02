from django.db.models import Manager


class BaseManager(Manager):
    """
    A custom manager that filters common fields
    """
    def __init__(self, *args, **kwargs):
        self.all_objects = kwargs.pop("all_objects", False)
        super().__init__(*args, **kwargs)

    @staticmethod
    def filter_archived(queryset):
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
    pass


class ProductVariantManager(BaseManager):
    """
    Custom manager of :model:`products.Product`
    """
    pass
