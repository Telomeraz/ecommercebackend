from django.urls import path

from .views import ListProductView, CreateProductView, UpdateProductView

urlpatterns = [
    path("", ListProductView.as_view()),
    path("create/", CreateProductView.as_view()),
    path("update/<int:pk>", UpdateProductView.as_view()),
]
