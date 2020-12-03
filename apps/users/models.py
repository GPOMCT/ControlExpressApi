from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from ..places.models import Place
from ..places.managers import PlaceUserManager
from ..actions.models import Action
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTROS')
    )

    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
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

    def __str__(self):
        return str(self.id) + ' - ' + self.user.email + ' - ' + self.place.name

    class Meta:
        db_table = "place_user"


class ActionPlace(models.Model):
    place_user = models.ForeignKey(PlaceUser, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.action.name + ' - '

    class Meta:
        db_table = "action_place"
