from rest_framework.generics import ListAPIView

from .serializers import CountrySerializer
from accounts.models import Country


class ListCountryView(ListAPIView):
    """
    API endpoint that allows countries to be viewed.
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
