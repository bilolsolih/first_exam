from django.db import models
from apps.common.models import BaseModel


class Service(BaseModel):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
