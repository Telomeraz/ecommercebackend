from django.urls import path

from .views import ListProductView, CreateProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    path("v1/", ListProductView.as_view()),
    path("v1/create/", CreateProductView.as_view()),
    path("v1/update/<int:pk>", UpdateProductView.as_view()),
    path("v1/delete/<int:pk>", DeleteProductView.as_view()),
]
