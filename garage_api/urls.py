from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from garage_api import views


router = DefaultRouter()
router.register('parts', views.PartModelViewSet, basename='parts') # api/parts/

urlpatterns = [
    path('cars/', include([
        path('', views.ListCreateCarAPIView.as_view(), name='car-list'),
        path('<int:pk>/', views.RetrieveUpdateDestroyCarAPIView.as_view(), name='car-detail'),
        path('stats/', views.CarStatsView.as_view(), name='car-stats'),
    ])),
    path('manufacturers/', views.ListCreateManufacturerAPIView.as_view(), name='manufacturer-list'),
] + router.urls