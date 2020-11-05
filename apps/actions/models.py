from django.db import models
from ..devices.models import Device


# Create your models here.

class Action(models.Model):
    name = models.CharField(max_length=30)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = "actions"
        verbose_name = "Action"
        verbose_name_plural = "Actions"
