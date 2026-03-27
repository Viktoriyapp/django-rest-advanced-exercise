from rest_framework import serializers
from garage_api.models import Manufacturer, Car, Part


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__' # Better specify the fields


class CarSerializer(serializers.ModelSerializer):
    # year = serializers.IntegerField(min_value=1900) # For model serializer, this validation is better to be in the model
    class Meta:
        model = Car
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'