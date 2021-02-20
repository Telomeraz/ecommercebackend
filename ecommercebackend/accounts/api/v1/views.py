from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .serializers import CountrySerializer
from accounts.models import Country
from utils.views import Authentication, SuperuserPermission


class ListCountryView(ListAPIView):
    """
    API endpoint that allows countries to be viewed.
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CreateUpdateDeleteCountryView(
    Authentication,
    SuperuserPermission,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
):
    """
    API endpoint that allows countries to be created, updated and deleted.
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
