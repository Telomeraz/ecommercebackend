from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import ArchiveMixin


class Courier(ArchiveMixin):
    """
    Stores infos of courier companies.
    """

    name = models.CharField(max_length=255, verbose_name=_("Courier name"))

    class Meta:
        verbose_name = _("Courier")
        verbose_name_plural = _("Couriers")

    def __str__(self):
        return self.name


class Shipment(models.Model):
    """
    Stores infos about shipment processes.
    """

    courier = models.ForeignKey(Courier, on_delete=models.PROTECT)

    tracking_code = models.CharField(max_length=255, verbose_name=_("Tracking code"))

    tracking_url = models.URLField(max_length=255, verbose_name=_("Tracking url"))

    fee = models.CharField(max_length=255, verbose_name=_("Shipment fee"))

    is_buyer_pays = models.BooleanField(default=False, verbose_name=_("Is the shipment buyer pays?"))

    class Meta:
        verbose_name = _("Shipment")
        verbose_name_plural = _("Shipments")

    def __str__(self):
        return "{} tracking code shipment".format(self.tracking_code)


class Package(models.Model):
    """
    Stands for packaging order lines. You can package one or more order lines
    by using this model for shipment processes.
    """

    shipment = models.ForeignKey(Shipment, blank=True, null=True, on_delete=models.SET_NULL)

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date and time"))

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return "Packaged at {}".format(self.created_datetime)
