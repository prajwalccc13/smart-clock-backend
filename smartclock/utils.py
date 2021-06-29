import RPi.GPIO as GPIO

from smartclock.models import Room, Device

def appliance(device_id, status, pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(pin, GPIO.OUT)


    if status == "True":
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.HIGH)



