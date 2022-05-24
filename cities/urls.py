from django.urls import path
from .views import CitiesListView

urlpatterns = [
    path('getcities/', CitiesListView.as_view())
]