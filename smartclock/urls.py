from django.urls import path

from smartclock.views import *

urlpatterns = [
    path("room/<int:pk>/device/", DeviceListCreateView.as_view(), name="device"),
    path("device/<int:pk>/", DeviceDetailView.as_view(), name="device_detail"),
    path("room/", RoomView.as_view(), name="room"),
    path("room/<int:pk>/", RoomDetailView.as_view(), name="rooms_detail"),
]