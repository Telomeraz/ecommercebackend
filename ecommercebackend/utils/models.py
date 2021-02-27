from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _


class ArchiveMixin(models.Model):
    """
    Use this abstract model when you have important data like product,
    product_variant etc. So, you won't delete objects, you'll archive them.
    """

    is_archived = models.BooleanField(
        default=False,
        help_text=_("This is a flag that represents whether deleted. True means deleted."),
    )

    class Meta:
        abstract = True

    def do_archive(self):
        """
        Archives instance of the model.
        """
        self.is_archived = True
        self.save()


class Currency(models.TextChoices):
    """
    Contains currency choices for prices.
    """

    USD = "USD", "$"
    EUR = "EUR", "€"
    TRY = "TRY", "₺"


class OwnerMixin(models.Model):
    """
    Stores owner generic relation. An owner can be an instance of
    :model:`accounts.User` or :model:`accounts.Customer`.
    """

    owner_limit = models.Q(app_label="accounts", model="customer") | models.Q(app_label="accounts", model="user")

    owner_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=owner_limit,
    )

    owner_object_id = models.PositiveIntegerField()

    owner = GenericForeignKey("owner_content_type", "owner_object_id")

    class Meta:
        abstract = True
