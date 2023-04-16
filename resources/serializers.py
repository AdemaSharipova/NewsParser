from rest_framework import serializers
from resources import models


class CreateResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Resource
        fields = (
            'resource_name',
            'resource_url',
            'top_tag',
            'bottom_tag',
            'title_cut',
            'date_cut',
        )


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Resource
        fields = '__all__'
