from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response

from products.models import Product, ProductVariant
from .serializers import (
    ListCreateProductSerializer,
    UpdateProductSerializer,
    CreateProductVariantSerializer,
    UpdateProductVariantSerializer,
)
from utils.views import Authentication, DefaultSuperuserPermission


class ListProductView(ListAPIView):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Product.objects.all()
    serializer_class = ListCreateProductSerializer


class CreateProductView(Authentication, DefaultSuperuserPermission, CreateAPIView):
    """
    API endpoint that allows products to be created.
    """

    serializer_class = ListCreateProductSerializer


class UpdateProductView(Authentication, DefaultSuperuserPermission, UpdateAPIView):
    """
    API endpoint that allows products to be updated.
    """

    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer


class DeleteProductView(Authentication, DefaultSuperuserPermission, DestroyAPIView):
    """
    API endpoint that allows products to be deleted.
    """

    queryset = Product.objects.all()

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.do_archive()
        return Response(status=HTTP_204_NO_CONTENT)


class CreateProductVariantView(Authentication, DefaultSuperuserPermission, CreateAPIView):
    """
    API endpoint that allows product variants to be created.
    """

    serializer_class = CreateProductVariantSerializer


class UpdateProductVariantView(Authentication, DefaultSuperuserPermission, UpdateAPIView):
    """
    API endpoint that allows product variants to be updated.
    """

    queryset = ProductVariant.objects.all()
    serializer_class = UpdateProductVariantSerializer


class DeleteProductVariantView(Authentication, DefaultSuperuserPermission, DestroyAPIView):
    """
    API endpoint that allows product variants to be deleted.
    """

    queryset = ProductVariant.objects.all()

    def delete(self, request, *args, **kwargs):
        product_variant = self.get_object()
        product_variant.do_archive()
        return Response(status=HTTP_204_NO_CONTENT)
