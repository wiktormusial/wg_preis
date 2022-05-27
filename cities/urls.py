from django.urls import path
from .views import CitiesListView, CitiesFavListView, CitiesDetailView

urlpatterns = [
    path('getcities/', CitiesListView.as_view()),
    path('getcity/<slug:slug>/', CitiesDetailView.as_view()),
    path('getfavcities/', CitiesFavListView.as_view())
]
