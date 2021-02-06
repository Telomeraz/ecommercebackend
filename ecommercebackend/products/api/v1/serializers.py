from django.http import Http404

from rest_framework.serializers import ModelSerializer, IntegerField

from ...models import Product, ProductVariant


class BaseProductVariantSerializer(ModelSerializer):
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

    variants = BaseProductVariantSerializer(many=True)

    def create(self, validated_data):
        """
        Creates product and its variants
        """
        variants = validated_data.pop("variants")
        product = Product.objects.create(product=validated_data, variants=variants)
        return product


class UpdateProductSerializer(BaseProductSerializer):
    """
    Serializes :model:`products.Product` fields for updating products.
    """

    variants = BaseProductVariantSerializer(many=True, read_only=True, required=False)


class CreateProductVariantSerializer(ModelSerializer):
    """
    Serializes :model:`products.ProductVariant` and product_id which
    represents product id of variant
    """

    product_id = IntegerField()

    class Meta:
        model = ProductVariant
        fields = (
            "id",
            "barcode",
            "price",
            "purchase_price",
            "list_price",
            "stock",
            "product_id",
            "created_datetime",
            "is_primary",
            "is_active",
        )

    def create(self, validated_data):
        """
        Creates variant based on product (instance of :model:`products.Product`)
        """
        product = validated_data.pop("product")
        product_variant = ProductVariant.objects.create(variant=validated_data, product=product)
        return product_variant

    def validate(self, attrs):
        """
        Validates received product_id and queries a product exist or not and
        if exists, sends product object in attrs which will be received in
        validated_data in create function
        """
        product_id = attrs.pop("product_id")
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404

        attrs["product"] = product
        return attrs


class UpdateProductVariantSerializer(BaseProductVariantSerializer):
    """
    Serializes :model:`products.ProductVariant` fields for updating product
    variants.
    """

    pass
