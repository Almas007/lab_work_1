from django.shortcuts import render
from parcers_v1.models import Resource, Items
from rest_framework import routers, viewsets
from parcers_v1.serializer import ResourceSerializer, ItemsSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

router = routers.DefaultRouter()
router.register(r'resource', ResourceViewSet)
router.register(r'items', ItemsViewSet)

