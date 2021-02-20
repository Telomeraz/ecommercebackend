import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


def _get_storage_path(instance, filename):
    return "images/{}/{}/{}".format(instance.content_type.model, uuid.uuid4(), filename)


class Image(models.Model):
    image = models.ImageField(upload_to=_get_storage_path)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey()

    def __str__(self):
        return "{}'s image. ID: {}".format(self.content_object, self.id)
