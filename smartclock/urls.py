from django.urls import path

from smartclock.views import *

urlpatterns = [
    path("device/", DeviceListView.as_view(), name="device"),
    path("device/detail/<int:pk>", DeviceDetailView.as_view(), name="device_detail"),
    path("room/", RoomListView.as_view(), name="room"),
    path("room/detail/<int:pk>", RoomDetailView.as_view(), name="rooms_detail"),
]