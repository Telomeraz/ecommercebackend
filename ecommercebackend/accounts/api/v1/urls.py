from django.urls import path

from .views import ListCountryView, CreateUpdateDeleteCountryView


urlpatterns = [
    path("countries/", ListCountryView.as_view()),
    path("countries/create/", CreateUpdateDeleteCountryView.as_view()),
    path("countries/update/<int:pk>/", CreateUpdateDeleteCountryView.as_view()),
    path("countries/delete/<int:pk>/", CreateUpdateDeleteCountryView.as_view()),
]
