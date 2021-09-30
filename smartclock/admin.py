from django.contrib import admin

from smartclock.models import Alarm, AutomatedTask, Room, Device, Task

admin.site.register(Room)
admin.site.register(Device)
admin.site.register(Alarm)
admin.site.register(AutomatedTask)
admin.site.register(Task)
