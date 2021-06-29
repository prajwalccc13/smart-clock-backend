from django.db import models


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