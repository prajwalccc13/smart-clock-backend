import requests
import json

# status_change = "turn off"
status_change = "turn on"
room = "kitchen"
appliance = "bulb"

status_flag = False
room_flag = False
device_flag = False



if status_change == "turn on" or status_change == "turn off": 
    status_flag = True
    if status_change == 'turn on':
        status_temp = True
    if status_change == 'turn off':
        status_temp = False
else:
    status_flag = False
    message = "Couldn't recognize the voice. Please say again."


# if - check if all data are provided
if status_flag:
    if status_change and room and appliance:
        
        # For Rooms
        rooms = requests.get('http://192.168.1.15:8000/api/room/').json()
        if rooms:
            for data in rooms:
                # Check if provided room is added in database
                if data['name'].lower() == room:
                    room_flag = True
                    room_id = data['id']

                    break
            else:
                room_flag = False
                message = "No rooms named " + room + " found. Please check and say again"
        else:
            room_flag = False
            message = "No rooms added. Please add rooms first."
    else:
        room_flag = False
        message = "Couldn't recognize the voice. Please say again."


# Fetch all devices
if room_flag:
    device_url = 'http://192.168.1.15:8000/api/room/' + str(room_id) + '/device/'
    device = requests.get(device_url).json()

    if device:
        # Check if provided device is added in database
        for data in device:
            # if device is available
            if data['name'].lower() == appliance:
                device_flag = True
                device_id = data['id']
                if status_temp:
                    if status_temp == data['status']:
                        message = room + " " + appliance + " already turned on."
                    else:
                        device_detail_url = 'http://192.168.1.15:8000/api/device/' + str(device_id) + '/'
                        device_patch = requests.patch(device_detail_url, data ={
                            'status': True,
                            'pin': int(data['pin'])
                        })
                        print('inside true')
                        # message = "Turning on the " + room + " " + appliance
                        if device_patch.status_code == 200:
                            message = "Turned on the " + room + " " + appliance
                        else: 
                            message = "Couldn't turn on the " + room + " " + appliance + ". Please try again."
                else:
                    if status_temp == data['status']:
                        message = room + " " + appliance + " already turned off."
                    else:
                        device_detail_url = 'http://192.168.1.15:8000/api/device/' + str(device_id) + '/'
                        device_patch = requests.patch(device_detail_url, data ={
                            'status': False,
                            'pin': int(data['pin'])
                        })
                        print('inside false')
                        # message = "Turning on the " + room + " " + appliance
                        if device_patch.status_code == 200:
                            message = "Turned off the " + room + " " + appliance
                        else: 
                            message = "Couldn't turn off the " + room + " " + appliance + ". Please try again."      
        if not device_flag:
            message = "No device named " + appliance + ' found.'
    else:
        message = "No devices added in " + room + " . Please add devices first."                    

print(message)
