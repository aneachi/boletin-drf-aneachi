from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf.vehiculos import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'marca', views.MarcaViewSet, basename='marca')
router.register(r'vehiculo', views.VehiculoViewSet, basename='vehiculo')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]