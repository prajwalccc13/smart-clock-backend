from rest_framework import serializers

from smartclock.models import Alarm, AutomatedTask, Room, Device, Task


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'icon_data']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'status', 'room', 'icon_data', 'pin']


class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = '__all__'


class AutomatedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomatedTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'