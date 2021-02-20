from django.utils.translation import gettext_lazy as _

from rest_framework.serializers import ModelSerializer, IntegerField, CharField
from rest_framework.validators import ValidationError

from products.models import (
    Product,
    ProductVariant,
    Attribute,
    AttributeValue,
    VarianterAttribute,
    VarianterAttributeValue,
)

from .validators import validate_attribute_values, validate_varianter_attribute_values


class AttributeSerializer(ModelSerializer):

    id = IntegerField()

    name = CharField(read_only=True)

    class Meta:
        model = Attribute
        fields = ("id", "name")


class AttributeValueSerializer(ModelSerializer):

    id = IntegerField()

    name = CharField(read_only=True)

    attribute = AttributeSerializer()

    class Meta:
        model = AttributeValue
        fields = ("id", "name", "attribute")


class VarianterAttributeSerializer(ModelSerializer):

    id = IntegerField()

    name = CharField(read_only=True)

    class Meta:
        model = VarianterAttribute
        fields = ("id", "name")


class VarianterAttributeValueSerializer(ModelSerializer):

    id = IntegerField()

    name = CharField(read_only=True)

    varianter_attribute = VarianterAttributeSerializer()

    class Meta:
        model = VarianterAttributeValue
        fields = ("id", "name", "varianter_attribute")


class BaseProductSerializer(ModelSerializer):
    """
    Base :model:`products.Product` serializer which is using for creating,
    updating etc.
    """

    values = AttributeValueSerializer(many=True, required=False)

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
            "values",
            "created_datetime",
            "is_active",
        )


class BaseProductVariantSerializer(ModelSerializer):

    values = VarianterAttributeValueSerializer(many=True, required=False)

    class Meta:
        model = ProductVariant
        fields = (
            "id",
            "barcode",
            "price",
            "purchase_price",
            "list_price",
            "stock",
            "values",
            "created_datetime",
            "is_primary",
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
        product = Product.objects.create(product=validated_data)
        return product

    def validate(self, attrs):
        """
        Validates received attrs (dict).
        """
        attrs = validate_attribute_values(attrs)
        attrs = validate_varianter_attribute_values(attrs)
        return attrs


class UpdateProductSerializer(BaseProductSerializer):
    """
    Serializes :model:`products.Product` fields for updating products.
    """

    variants = BaseProductVariantSerializer(many=True, read_only=True, required=False)

    def update(self, instance, validated_data):
        instance.update(validated_data)
        return instance

    def validate(self, attrs):
        attrs = validate_attribute_values(attrs)
        return attrs


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
        product_variant = ProductVariant.objects.create(variant=validated_data)
        return product_variant

    def validate(self, attrs):
        """
        Validates product_id received and queries a product exist or not and
        if exists, sends product object in attrs which will be received in
        validated_data in create function
        """
        product_id = attrs.pop("product_id")
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError(_("Product not found with id %s" % product_id))

        attrs["product"] = product
        return attrs


class UpdateProductVariantSerializer(BaseProductVariantSerializer):
    """
    Serializes :model:`products.ProductVariant` fields for updating product
    variants.
    """

    pass
