from rest_framework import serializers
from .models import Place
from ..users.models import PlaceUser, User, ActionPlace
from ..actions.serializers import ActionSerializer


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'description',
        )


class ActionPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPlace
        fields = '__all__'


class UserPlaceSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    actions = ActionSerializer(many=True)

    class Meta:
        model = PlaceUser
        fields = (
            'is_admin',
            'place',
            'actions',
        )
