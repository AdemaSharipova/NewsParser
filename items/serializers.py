from rest_framework import serializers
from items import models


class CreateItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = ('res_id',)


class ListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = '__all__'
