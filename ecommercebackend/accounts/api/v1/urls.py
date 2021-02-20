from django.urls import path

from .views import (
    ListCountryView,
    CreateUpdateDeleteCountryView,
    ListCityView,
    CreateCityView,
    UpdateDeleteCityView,
)


urlpatterns = [
    path("countries/", ListCountryView.as_view()),
    path("countries/create/", CreateUpdateDeleteCountryView.as_view()),
    path("countries/update/<int:pk>/", CreateUpdateDeleteCountryView.as_view()),
    path("countries/delete/<int:pk>/", CreateUpdateDeleteCountryView.as_view()),
    path("cities/", ListCityView.as_view()),
    path("cities/create/", CreateCityView.as_view()),
    path("cities/update/<int:pk>/", UpdateDeleteCityView.as_view()),
    path("cities/delete/<int:pk>/", UpdateDeleteCityView.as_view()),
]
