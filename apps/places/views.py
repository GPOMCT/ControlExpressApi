from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .models import Place
from ..users.models import User, PlaceUser
from ..users.permissions import IsOwner
from .serializers import PlaceSerializer, UserPlaceSerializer


# Create your views here.
# class PlaceUserListApiView(generics.ListAPIView):
#
#     def get_queryset(self):
#         return Place.objects.all()

class ListPlaceUser(generics.ListAPIView):
    pass


class PlacesListApiView(generics.ListAPIView):
    serializer_class = UserPlaceSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self):
        pass
        # user = self.request.user
        # return PlaceUser.objects.place_user(user)
        # return PlaceUser.objects.all()
