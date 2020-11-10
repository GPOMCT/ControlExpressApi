from django.db import models


class PlaceUserManager(models.Manager):
    def place_user(self, user):
        return self.filter(
            user=user,
        )
