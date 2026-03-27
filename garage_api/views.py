from django.db.models.aggregates import Count, Min, Max
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from garage_api.models import Car, Manufacturer, Part
from garage_api.serializers import CarSerializer, ManufacturerSerializer, PartSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class ListCreateCarAPIView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ListCreateManufacturerAPIView(ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class RetrieveUpdateDestroyCarAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class PartModelViewSet(ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class CarStatsView(APIView):
    def get(self, request: Request) -> Response:
        stats = Car.objects.aggregate(
            total_cars=Count('id'),
            oldest_year=Min('year'),
            newest_year=Max('year')
        )
        return Response(stats, status=status.HTTP_200_OK)