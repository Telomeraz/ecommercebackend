from django.urls import path

from .views import ListProductView, CreateProductView

urlpatterns = [
    path("", ListProductView.as_view()),
    path("create/", CreateProductView.as_view()),
]
