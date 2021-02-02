from rest_framework.generics import ListAPIView

from ...models import Product
from .serializers import ProductSerializer


class ListProductView(ListAPIView):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Product.objects.all().order_by("-created_datetime")
    serializer_class = ProductSerializer
