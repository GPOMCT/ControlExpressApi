from django.urls import path
from .views import PlacesListApiView

urlpatterns = [
    path('', PlacesListApiView.as_view(), name="places"),
]