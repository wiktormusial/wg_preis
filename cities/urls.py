from django.urls import path
from .views import CitiesListView, CitiesFavListView

urlpatterns = [
    path('getcities/', CitiesListView.as_view()),
    path('getfavcities/', CitiesFavListView.as_view())
]
