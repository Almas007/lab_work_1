from rest_framework import serializers
from parcers_v1 import models


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        fields = '__all__'
        #fields = ['id', 'resource_name', 'resource_url', 'top_tag', 'bottom_tag', 'title_cut', 'date_cut']
        read_only_fields = ['id']

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Items
        fields = '__all__'
        #fields = ['id', 'res_id', 'link', 'title', 'content', 'nd_date', 's_date', 'not_date']
        read_only_fields = ['id', 'res_id']