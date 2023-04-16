import uuid

from django.db import models


class Resource(models.Model):
    resource_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    resource_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=None
    )
    resource_url = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default=None
    )
    top_tag = models.JSONField()
    bottom_tag = models.JSONField()
    title_cut = models.JSONField()
    date_cut = models.JSONField()


