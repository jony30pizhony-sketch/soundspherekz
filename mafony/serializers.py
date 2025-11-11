from rest_framework import serializers
from .models import AndroidHeadUnit

class HeadUnitSerializer(serializers.ModelSerializer):
    manufacturer_name = serializers.CharField(source='manufacturer.name', read_only=True)
    country_name = serializers.CharField(source='country.name', read_only=True)
    
    class Meta:
        model = AndroidHeadUnit
        fields = [
            'id', 'name', 'manufacturer_name', 'country_name', 
            'screen_size', 'price', 'description', 'android_version',
            'ram', 'storage', 'image', 'in_stock'
        ]