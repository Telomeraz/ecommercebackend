from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response

from ...models import Product, ProductVariant
from .serializers import (
    ListCreateProductSerializer,
    UpdateProductSerializer,
    CreateProductVariantSerializer,
    UpdateProductVariantSerializer,
)


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
    API endpoint that allows products to be updated.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = Product.objects.all().order_by("-created_datetime")
    serializer_class = UpdateProductSerializer


class DeleteProductView(DestroyAPIView):
    """
    API endpoint that allows products to be deleted.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = Product.objects.all().order_by("-created_datetime")

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.do_archive()
        return Response(status=HTTP_204_NO_CONTENT)


class CreateProductVariantView(CreateAPIView):
    """
    API endpoint that allows product variants to be created.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    serializer_class = CreateProductVariantSerializer


class UpdateProductVariantView(UpdateAPIView):
    """
    API endpoint that allows product variants to be updated.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = ProductVariant.objects.all().order_by("-created_datetime")
    serializer_class = UpdateProductVariantSerializer
