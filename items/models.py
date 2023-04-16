import uuid

from django.db import models


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    res_id = models.ForeignKey(
        to='resources.Resource',
        on_delete=models.SET_NULL,
        null=True,
        related_name='resources',
    )
    link = models.CharField(max_length=255)
    title = models.TextField()
    content = models.TextField()
    nd_date = models.IntegerField(null=True)
    not_date = models.DateField(null=True)

    s_date = models.DateTimeField(auto_now_add=True)

