from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    """
    Stores country's infos.
    """

    name = models.CharField(max_length=255, unique=True, verbose_name=_("Country Name"))

    alpha2_code = models.CharField(max_length=2, unique=True, verbose_name=_("Alpha-2 Code"))

    alpha3_code = models.CharField(max_length=3, unique=True, verbose_name=_("Alpha-3 Code"))

    numeric_code = models.PositiveSmallIntegerField(
        validators=(validators.MaxValueValidator(999),),
        unique=True,
        verbose_name=_("Numeric Code"),
    )

    def __str__(self):
        return self.name
