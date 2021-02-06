from django.urls import path

from .views import (
    ListProductView,
    CreateProductView,
    UpdateProductView,
    DeleteProductView,
    CreateProductVariantView,
    UpdateProductVariantView,
    DeleteProductVariantView,
)

urlpatterns = [
    path("", ListProductView.as_view()),
    path("create/", CreateProductView.as_view()),
    path("update/<int:pk>/", UpdateProductView.as_view()),
    path("delete/<int:pk>/", DeleteProductView.as_view()),
    path("variants/create/", CreateProductVariantView.as_view()),
    path("variants/update/<int:pk>/", UpdateProductVariantView.as_view()),
    path("variants/delete/<int:pk>/", DeleteProductVariantView.as_view()),
]
