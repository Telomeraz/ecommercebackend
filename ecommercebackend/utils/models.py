from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseArchive(models.Model):
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
