from django.urls import path

from .views import CountryView, CityView


urlpatterns = [
    path("countries/", CountryView.as_view()),
    path("countries/<int:pk>/", CountryView.as_view()),
    path("cities/", CityView.as_view()),
    path("cities/<int:pk>/", CityView.as_view()),
]
