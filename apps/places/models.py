from django.db import models
from ..accounts.models import Account


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, default=None)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, default=None)

    class Meta:
        db_table = "places"
        verbose_name = "Place"
        verbose_name_plural = "Places"
