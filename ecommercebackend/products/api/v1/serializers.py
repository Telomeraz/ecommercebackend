from rest_framework.serializers import ModelSerializer

from ...models import Product, ProductVariant


class ProductVariantSerializer(ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = (
            "id",
            "barcode",
            "price",
            "purchase_price",
            "list_price",
            "stock",
            "created_datetime",
            "is_primary",
            "is_active",
        )


class BaseProductSerializer(ModelSerializer):
    """
    Base :model:`products.Product` serializer which is using for creating,
    updating etc.
    """
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "subheading",
            "description",
            "currency",
            "tax_rate",
            "variants",
            "created_datetime",
            "is_active",
        )


class ListCreateProductSerializer(BaseProductSerializer):
    """
    Serializes :model:`products.Product` and :model:`products.ProductVariant`
    fields for listing and creating products.
    """
    variants = ProductVariantSerializer(many=True)

    def create(self, validated_data):
        """
        Creates product and its variants
        """
        variants = validated_data.pop("variants")
        product = Product.objects.create(validated_data, variants=variants)
        return product


class UpdateProductSerializer(BaseProductSerializer):
    """
    Serializes :model:`products.Product` fields for listing and creating
    products.
    """
    variants = ProductVariantSerializer(many=True, read_only=True, required=False)
