from django.urls import path

from smartclock.views import *

urlpatterns = [
    path("room/<int:pk>/device/", DeviceListCreateView.as_view(), name="device"),
    path("device/<int:pk>/", DeviceDetailView.as_view(), name="device_detail"),
    path("room/", RoomView.as_view(), name="room"),
    path("room/<int:pk>/", RoomDetailView.as_view(), name="rooms_detail"),
    path("alarm/", AlarmView.as_view(), name='alarm-create-list'),
    path("alarm/<int:pk>/", EditAlarm.as_view(), name='alarm-edit'),
    path("automated-task/", AutomatedTaskView.as_view(), name='automated-task-list-create'),
    path("automated-task/<int:pk>/", EditAutomatedTask.as_view(), name='automated-task-edit'),
    path("task/", TaskView.as_view(), name='task-list-create'),
    path("task/<int:pk>/", TaskView.as_view(), name='task-list-create'),
    path("automated-task/<int:pk>/tasks/", TaskList.as_view(), name='task-list'),
]