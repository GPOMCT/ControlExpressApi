from django.db import models
from ..devices.models import Device


# Create your models here.

# class Type(models.Model):
#     pass


class Action(models.Model):
    TYPE_CHOICES = (
        ('Door', 'Door'),
        ('Garage', 'Garage'),
        ('Window', 'Window'),
        ('Light', 'Light'),
    )
    name = models.CharField(max_length=30)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, default=None)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "actions"
        verbose_name = "Action"
        verbose_name_plural = "Actions"
