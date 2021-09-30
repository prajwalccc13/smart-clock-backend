from django.shortcuts import render

from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import status

from smartclock.serializers import AlarmSerializer, AutomatedTaskSerializer, RoomSerializer, DeviceSerializer, TaskSerializer
from smartclock.models import Alarm, AutomatedTask, Room, Device, Task

from smartclock.utils import *
import smartclock.scripts.flagValues as flag_values


class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def post(self, request):
        data = request.data
        name = data['name']
        icon_data = data['icon_data']
        room = Room.objects.create(
            name=name,
            icon_data=icon_data
        )
        room.save()
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        rooms_all = Room.objects.all()
        serializer = RoomSerializer(rooms_all, many=True)
        return Response(serializer.data)


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "pk"
        

class DeviceListCreateView(views.APIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def post(self, request, pk):
        data = request.data
        name = data['name']
        device_status = data['status']
        icon_data = data['icon_data']
        # room = data['room']
        pin = data['pin']
        room = Room.objects.get(pk=pk)
        device = Device.objects.create(
            name=name,
            status=device_status,
            icon_data=icon_data,
            room=room,
            pin=pin,
        )
        serializer = DeviceSerializer(device, many=False)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        try:
            room = Room.objects.get(pk=pk)
            device = Device.objects.filter(room=room)
            serializer = DeviceSerializer(device, many=True)
            return Response(serializer.data)
        except Device.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = "pk"

    def patch(self, request, pk):
        device = Device.objects.get(pk=pk)
        serializer = DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(request.data['status'])
            print(type(request.data['status']))
            statuS = request.data['status']
            if request.data['status'] == 'True':
                statuS = True
            if request.data['status'] == 'False':
                statuS = False
            appliance(pk,statuS, request.data['pin'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlarmView(generics.ListCreateAPIView):
    queryset = Alarm.objects.all()
    flag_values.setAlarmFlag()
    serializer_class = AlarmSerializer

class EditAlarm(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alarm.objects.all()
    flag_values.setAlarmFlag()
    serializer_class = AlarmSerializer


class AutomatedTaskView(generics.ListCreateAPIView):
    queryset = AutomatedTask.objects.all()
    serializer_class = AutomatedTaskSerializer

class EditAutomatedTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = AutomatedTask.objects.all()
    serializer_class = AutomatedTaskSerializer


class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class EditTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskList(views.APIView):
    def get(self, request, pk):
        tasks = Task.objects.filter(automatedtask= pk)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class DoTask(views.APIView):
    def get(self,request, pk):
        tasks = Task.objects.filter(automatedtask=pk)
        for task in tasks:
            device = Device.objects.get(id=task.device.id)
            if task.status:
                appliance(pk,task.to_do, device.pin)
        return Response(data="Success")
