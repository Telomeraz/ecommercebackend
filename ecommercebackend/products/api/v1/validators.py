from django.http import Http404

from products.models import AttributeValue, VarianterAttributeValue


def validate_attribute_values(attrs):
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


def validate_varianter_attribute_values(attrs):
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
