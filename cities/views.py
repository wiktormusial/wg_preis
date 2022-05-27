from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CitySerializer
from .models import City


class CitiesListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitiesFavListView(generics.ListAPIView):
    queryset = City.objects.filter(isFav=True)
    serializer_class = CitySerializer

class CitiesDetailView(APIView):
    def get_object(self, slug):
        try:
            return City.objects.get(slug=slug)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        city = self.get_object(slug)
        serializer = CitySerializer(city)
        return Response(serializer.data)
