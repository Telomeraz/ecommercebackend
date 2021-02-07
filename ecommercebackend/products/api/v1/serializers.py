from django.http import Http404

from rest_framework.serializers import ModelSerializer, IntegerField, CharField

from ...models import (
    Product,
    ProductVariant,
    Attribute,
    AttributeValue,
    VarianterAttribute,
    VarianterAttributeValue,
)


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

    def _validate_attribute_values(self, attrs):
        """
        Validates attribute values and if they're valid, replaces attribute
        values ids with objects of :model:`products.AttributeValue` for
        product.
        """
        values = attrs.pop("values", [])
        attribute_values = []
        for value in values:
            attribute = value.get("attribute")
            try:
                attribute_value = AttributeValue.objects.get(
                    id=value.get("id"),
                    attribute_id=attribute.get("id"),
                )
            except AttributeValue.DoesNotExist:
                raise Http404
            attribute_values.append(attribute_value)
        attrs["attribute_values"] = attribute_values
        return attrs

    def _validate_varianter_attribute_values(self, attrs):
        """
        Validates varianter attribute values and if they're valid, replaces
        varianter attribute values ids with objects of
        :model:`products.VarianterAttributeValue` for variants.
        """
        variants = attrs.get("variants")
        for variant in variants:
            varianter_attribute_values = []
            values = variant.pop("values", [])
            for value in values:
                varianter_attribute = value.get("varianter_attribute")
                try:
                    varianter_attribute_value = VarianterAttributeValue.objects.get(
                        id=value.get("id"),
                        varianter_attribute_id=varianter_attribute.get("id"),
                    )
                except VarianterAttributeValue.DoesNotExist:
                    raise Http404
                varianter_attribute_values.append(varianter_attribute_value)
            variant["varianter_attribute_values"] = varianter_attribute_values
        return attrs

    def validate(self, attrs):
        """
        Validates received attrs (dict).
        """
        attrs = self._validate_attribute_values(attrs)
        attrs = self._validate_varianter_attribute_values(attrs)
        return attrs


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
