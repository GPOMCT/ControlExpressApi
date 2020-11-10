from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from django.contrib.auth.models import BaseUserManager
from ..places.models import Place
from ..places.managers import PlaceUserManager
from ..actions.models import Action


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    places = models.ManyToManyField(Place, through='PlaceUser')
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default='email')

    class Meta:
        db_table = "users"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class PlaceUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    actions = models.ManyToManyField(Action, through='ActionPlace')

    objects = PlaceUserManager()

    class Meta:
        db_table = "place_user"


class ActionPlace(models.Model):
    place_user = models.ForeignKey(PlaceUser, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "action_place"
