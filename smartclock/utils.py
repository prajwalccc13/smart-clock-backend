from smartclock.models import Room, Device

def appliance(device_id, status):
    if status == "True":
        print(str(device_id)+" is turned On")
    else:
        print(f'{device_id} is turned Off')

