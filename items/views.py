from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from items import models, serializers, services


class ItemsCreateAPIView(generics.CreateAPIView):
    services = services.ItemsServicesV1()

    queryset = models.Item.objects.all()
    serializer_class = serializers.CreateItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.services.parse(request.data)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ItemsListAPIView(generics.ListAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ListItemSerializer
