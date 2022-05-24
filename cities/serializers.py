from rest_framework import serializers
from .models import City, Price

class CitySerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ['id', 'city', 'slug', 'price', 'created_at']

    def get_price(self, obj):
        return Price.objects.filter(city=obj.id).last().price
