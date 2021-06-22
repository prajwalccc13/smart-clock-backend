from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=20)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=20)
    devices = models.ForeignKey(on_delete=models.CASCADE)

    def __str__(self):
        return self.name
