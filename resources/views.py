from rest_framework.viewsets import ModelViewSet

from resources import models, serializers
from utils import mixins


class ResourceViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    queryset = models.Resource.objects.all()
    ACTION_SERIALIZERS = {
        'create': serializers.CreateResourceSerializer,
    }
    serializer_class = serializers.ResourceSerializer
