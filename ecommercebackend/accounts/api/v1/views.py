from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView

from .serializers import CountrySerializer, ListUpdateCitySerializer, CreateCitySerializer
from accounts.models import Country, City
from utils.views import Authentication, DefaultSuperuserPermission


class CountryView(
    Authentication,
    DefaultSuperuserPermission,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
):
    """
    API endpoint that allows countries to be viewed, created, updated and
    deleted.
    """

    admin_methods = ("POST", "PUT", "PATCH", "DELETE")
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityView(
    Authentication,
    DefaultSuperuserPermission,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
):
    """
    API endpoint that allows cities to be viewed, created, updated and
    deleted.
    """

    admin_methods = ("POST", "PUT", "PATCH", "DELETE")
    queryset = City.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateCitySerializer
        return ListUpdateCitySerializer
