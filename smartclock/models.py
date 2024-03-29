from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

import smartclock.scripts.flagValues as flag_values 


class Room(models.Model):
    name = models.CharField(max_length=20)
    icon_data = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    status_choices = (
        (True, "On"),
        (False, "Off")
    )
    name = models.CharField(max_length=20)
    status = models.BooleanField("Device status", default=False, choices=status_choices)
    icon_data = models.IntegerField(null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    pin = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Alarm(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    hour = models.IntegerField()
    minute = models.IntegerField()
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    active = models.BooleanField()

    def __str__(self) -> str:
        return self.title + " - " + self.time


class AutomatedTask(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    hour = models.IntegerField()
    minute = models.IntegerField()
    active = models.BooleanField()

    def __str__(self) -> str:
        return self.title + " - " + self.time


class Task(models.Model):
    automatedtask = models.ForeignKey(AutomatedTask, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    # pin = models.IntegerField()
    to_do = models.BooleanField(default=False)
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.device.name + " - " + self.automatedtask.title 


@receiver([post_save, post_delete], sender=AutomatedTask)
def change_routine_flag(sender, instance, **kwargs):
    flag_values.setRoutineFlag()
    print("routine flag updated!")

@receiver([post_save, post_delete], sender=Alarm)
def change_alarm_flag(sender, instance, **kwargs):
    flag_values.setAlarmFlag()
    print("alarm flag updated!")
