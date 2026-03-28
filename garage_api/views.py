from django.db.models.aggregates import Count, Min, Max
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from garage_api.models import Car, Manufacturer, Part
from garage_api.serializers import CarSerializer, PartSerializer, ManufacturerNestedReadSerializer, \
    ManufacturerSerializer, CarNestedReadSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


# TODO: move to utils
class ReadWriteSerializerMixin:
    SAFE_METHODS = ['GET']

    read_serializer = None
    write_serializer = None

    def get_serializer_class(self):
        if self.request.method in self.SAFE_METHODS:
            return self.read_serializer
        return self.write_serializer


class ListCreateCarAPIView(ReadWriteSerializerMixin, ListCreateAPIView):
    queryset = Car.objects.select_related('manufacturer').prefetch_related('parts').all()
    read_serializer = CarNestedReadSerializer
    write_serializer = CarSerializer


class RetrieveUpdateDestroyCarAPIView(ReadWriteSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.select_related('manufacturer').prefetch_related('parts').all()
    read_serializer = CarNestedReadSerializer
    write_serializer = CarSerializer


class ListCreateManufacturerAPIView(ReadWriteSerializerMixin, ListCreateAPIView):
    queryset = Manufacturer.objects.prefetch_related('cars', 'parts').all()
    read_serializer = ManufacturerNestedReadSerializer
    write_serializer = ManufacturerSerializer


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