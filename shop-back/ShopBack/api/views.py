from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from . import serializers, models
import json


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


def categories_list(request, id):
    queryset = models.Product.objects.filter(category_id=id)
    prod_json = serializers.ProductSerializer(queryset, many=True)
    return HttpResponse(json.dumps(prod_json.data))
