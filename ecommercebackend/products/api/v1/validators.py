from django.utils.translation import gettext_lazy as _

from rest_framework.validators import ValidationError

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
        value_id = value.get("id")
        attribute_id = value.get("attribute").get("id")
        try:
            attribute_value = AttributeValue.objects.get(
                id=value_id,
                attribute_id=attribute_id,
            )
        except AttributeValue.DoesNotExist:
            raise ValidationError(
                _("Attribute value not found with id: %s and attribute_id: %s" % (value_id, attribute_id))
            )
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
            value_id = value.get("id")
            varianter_attribute_id = value.get("varianter_attribute").get("id")
            try:
                varianter_attribute_value = VarianterAttributeValue.objects.get(
                    id=value_id,
                    varianter_attribute_id=varianter_attribute_id,
                )
            except VarianterAttributeValue.DoesNotExist:
                raise ValidationError(
                    _(
                        "Varianter attribute value not found with id: %s and varianter_attribute_id: %s"
                        % (value_id, varianter_attribute_id)
                    )
                )
            varianter_attribute_values.append(varianter_attribute_value)
        variant["varianter_attribute_values"] = varianter_attribute_values
    return attrs
