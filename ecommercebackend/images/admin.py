from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Admin page of :model:`images.Image`
    """

    list_display = ("id", "content_type", "object_id", "content_object")
    search_fields = ("id", "content_type", "object_id", "content_object")
