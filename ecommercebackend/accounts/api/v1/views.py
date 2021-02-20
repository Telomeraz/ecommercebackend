from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .serializers import CountrySerializer, ListUpdateCitySerializer, CreateCitySerializer
from accounts.models import Country, City
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


class ListCityView(ListAPIView):
    """
    API endpoint that allows cities to be viewed.
    """

    queryset = City.objects.all()
    serializer_class = ListUpdateCitySerializer


class CreateCityView(Authentication, SuperuserPermission, CreateAPIView):
    """
    API endpoint that allows cities to be created.
    """

    serializer_class = CreateCitySerializer


class UpdateDeleteCityView(Authentication, SuperuserPermission, UpdateAPIView, DestroyAPIView):
    """
    API endpoint that allows cities to be updated and deleted.
    """

    queryset = City.objects.all()
    serializer_class = ListUpdateCitySerializer
