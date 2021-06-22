from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Device(models.Model):
    status_choices = (
        (True, "On"),
        (False, "Off")
    )
    name = models.CharField(max_length=20)
    status = models.BooleanField("Device status", default=False, choices=status_choices)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name