from django.urls import path

from .views import ListCountryView


urlpatterns = [
    path("", ListCountryView.as_view()),
]
