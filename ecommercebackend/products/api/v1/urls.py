from django.urls import path

from .views import ListProductView

urlpatterns = [
    path("", ListProductView.as_view()),
]
