import RPi.GPIO as GPIO

from smartclock.models import Room, Device

def appliance(device_id, status, pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(pin, GPIO.OUT)

    print(status)
    if status == "true":
        GPIO.output(pin, GPIO.LOW)
        print("inside true")
    else:
        GPIO.output(pin, GPIO.HIGH)
	print("inside false")



