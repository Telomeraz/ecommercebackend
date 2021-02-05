from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

from ...models import Product
from .serializers import ListCreateProductSerializer, UpdateProductSerializer


class ListProductView(ListAPIView):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Product.objects.all().order_by("-created_datetime")
    serializer_class = ListCreateProductSerializer


class CreateProductView(CreateAPIView):
    """
    API endpoint that allows products to be created.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    serializer_class = ListCreateProductSerializer


class UpdateProductView(UpdateAPIView):
    """
    API endpoint that allows products to be created.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = Product.objects.all().order_by("-created_datetime")
    serializer_class = UpdateProductSerializer
