from rest_framework.serializers import ModelSerializer

from accounts.models import Country


class CountrySerializer(ModelSerializer):
    """
    Serializes :model:`accounts.Country` fields for listing, creating.
    """

    class Meta:
        model = Country
        fields = ("id", "name", "alpha2_code", "alpha3_code", "numeric_code")
