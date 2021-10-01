from datetime import date, datetime
import time
import subprocess
import multiprocessing
import json
import requests

import flagValues


def alarm():
    url = 'http://192.168.1.15:8000/'
    while True:
        routineFlagJson = open('smartclock/scripts/routineFlag.json')
        routineFlag = json.load(routineFlagJson)

        # Retrive all routine data when any change occur in routine model
        # print('here----' + str(routineFlag['routine_flag']))
        # print(routineFlag)
        if(routineFlag['routine_flag']):
            routine_data = []
            does_routine_have_data = False
            routine_list_url = url + 'api/automated-task/'
            routine_list = requests.get(routine_list_url).json()
            # print('here!!!!!!!')

            for data in routine_list:
                if data['active']:
                    routine_data.append({
                        'id': data['id'],
                        'hour': data['hour'],
                        'minute': data['minute'],
                    })
                    does_routine_have_data = True
                    # print('here@@@@@@')
            flagValues.unsetRoutineFlag()

        now = datetime.now()
        time_hour = int(now.strftime("%H"))
        time_minute = int(now.strftime("%M"))
        time_second = int(now.strftime("%S"))

        # print(str(now) + '----------------')
        # print(str(routine_data) + '+++++++++++++++++++')
        if does_routine_have_data:
            for routine in routine_data:
                # print('here')
                # print(str(routine) + '+++++++++++++++++++')
                if(time_hour == routine['hour'] and time_minute == routine['minute'] and time_second == 0):
                    print(routine['hour'])
                    print(routine['minute'])
                    print(routine['id'])
                    print('---------')
                    do_routine_url = url + 'api/automated-task/' + routine[id] + '/do/'
                    do_routine_response = requests.get(do_routine_url).json()
                    print('--------' + str(do_routine_response))
                # print(routine)

        time.sleep(1)
        


# days = {
#     'sunday': True,
#     'monday': True,
#     'tuesday': True,
#     'wednesday': True,
#     'thursday': True,
#     'friday': True,
#     'saturday': True,
# }
# alarmTime = "23:30"
alarm()