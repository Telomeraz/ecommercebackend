from django.utils.translation import gettext_lazy as _

from rest_framework.serializers import ModelSerializer, IntegerField
from rest_framework.validators import ValidationError

from accounts.models import Country, City


class CountrySerializer(ModelSerializer):
    """
    Serializes :model:`accounts.Country` fields.
    """

    class Meta:
        model = Country
        fields = ("id", "name", "alpha2_code", "alpha3_code", "numeric_code")


class ListUpdateCitySerializer(ModelSerializer):
    """
    Serializes :model:`accounts.City` fields for listing and updating.
    """

    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ("id", "name", "country")


class CreateCitySerializer(ModelSerializer):
    """
    Serializes :model:`accounts.City` fields for creating.
    """

    country_id = IntegerField()

    class Meta:
        model = City
        fields = ("id", "name", "country_id")

    def create(self, validated_data):
        """
        Creates city
        """
        city = City.objects.create(**validated_data)
        return city

    def validate(self, attrs):
        """
        Validates if a country exists with country_id received
        """
        country_id = attrs.pop("country_id")
        try:
            country = Country.objects.get(id=country_id)
        except Country.DoesNotExist:
            raise ValidationError(_("Country not found with id %s" % country_id))

        attrs["country"] = country
        return attrs
