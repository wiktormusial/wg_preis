from rest_framework import generics
from .serializers import CitySerializer
from .models import City


class CitiesListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer