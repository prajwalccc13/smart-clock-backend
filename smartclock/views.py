from django.shortcuts import render

from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import status

from smartclock.serializers import RoomSerializer, DeviceSerializer
from smartclock.models import Room, Device

from smartclock.utils import *


class RoomListView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "pk"
        

class DeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = "pk"

    def patch(self, request, pk):
        device = Device.objects.get(pk=pk)
        serializer = DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            appliance(pk,request.data["status"])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
