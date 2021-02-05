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
    variants = ProductVariantSerializer(many=True)

    def create(self, validated_data):
        variants = validated_data.pop("variants")
        product = Product.objects.create(validated_data, variants=variants)
        return product


class UpdateProductSerializer(BaseProductSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True, required=False)
