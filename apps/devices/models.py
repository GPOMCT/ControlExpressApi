from django.db import models
from ..places.models import Place


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=30)
    unique_id = models.CharField(max_length=30)
    sn = models.CharField(max_length=30, default=None)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "devices"
        verbose_name = "Device"
        verbose_name_plural = "Devices"

