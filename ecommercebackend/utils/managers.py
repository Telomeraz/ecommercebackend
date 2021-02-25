from django.contrib.auth import get_user_model
from django.db import models


class ArchiveManager(models.Manager):
    """
    Custom manager that filters common fields.
    """

    def __init__(self, *args, **kwargs):
        self.all_objects = kwargs.pop("all_objects", False)
        super().__init__(*args, **kwargs)

    def _filter_archived(self, queryset):
        """
        Filters queryset by is_archived field
        """
        return queryset.exclude(is_archived=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.all_objects:
            return queryset
        return self._filter_archived(queryset)


class OwnerManager(models.Manager):
    """
    Contains customer filters for models which inherit
    :model:`utils.OwnerMixin`.
    """
    def filter_by_owner(self, owner):
        if isinstance(owner, get_user_model()) and owner.is_superuser:
            return self.get_queryset()
        return self.get_queryset().filter(owner=owner)
