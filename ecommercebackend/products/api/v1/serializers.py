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


class ProductSerializer(ModelSerializer):
    variants = ProductVariantSerializer(many=True)

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

    def create(self, validated_data):
        variants = validated_data.pop('variants')
        product = Product.objects.create(validated_data, variants=variants)
        return product
