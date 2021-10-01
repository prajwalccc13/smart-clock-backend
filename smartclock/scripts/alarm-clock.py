from datetime import date, datetime
import time
import subprocess
import multiprocessing
import json
import requests

from playsound import playsound
import flagValues


# subprocess.call(['mpg123', "welcome.mp3"])

"""
time - 22:55:33 (HH:MM:DD)
days - {
    sunday - True,
    monday - True,
    tuesday - True,
    wednesday - True,
    thursday - True,
    friday - True,
    saturday - True,
}
"""

flagValues.setRoutineFlag()


def alarm():
    day_check = {
        'sunday': False,
        'monday': False,
        'tuesday': False,
        'wednesday': False,
        'thursday': False,
        'friday': False,
        'saturday': False,
    }
    url = 'http://192.168.1.9:8000/api/alarm'
    while True:
        alarmFlagJson = open('smartclock/scripts/alarmFlag.json')
        alarmFlag = json.load(alarmFlagJson)

        if(alarmFlag['alarm_flag']):
            x = requests.get(url).json()
            sunday = []
            monday = []
            tuesday = []
            wednesday = []
            thursday = []
            friday = []
            saturday = []
            day_check = {
                'sunday': False,
                'monday': False,
                'tuesday': False,
                'wednesday': False,
                'thursday': False,
                'friday': False,
                'saturday': False,
            }
            days_time = {}


            for data in x:
                if data['active']:
                    if data['sunday']:
                        sunday.append({
                            'id': data['id'],
                            'hour': data['hour'],
                            'minute': data['minute'],
                        })
                        day_check['sunday'] = True
                    if data['monday']:
                        monday.append({
                            'id': data['id'],
                            'hour': data['hour'],
                            'minute': data['minute'],
                        })
                        day_check['monday'] = True
                    if data['tuesday']:
                        tuesday.append({
                            'id': data['id'],
                            'hour': data['hour'],
                            'minute': data['minute'],
                        })
                        day_check['tuesday'] = True
                    if data['wednesday']:
                        wednesday.append({
                            'id': data['id'],
                            'hour': data['hour'],
                            'minute': data['minute'],
                        })
                        day_check['wednesday'] = True
                    if data['thursday']:
                        thursday.append({
                            'id': data['id'],
                            'hour': data['hour'],
                            'minute': data['minute'],
                        })
                        day_check['thursday'] = True
                    if data['friday']:
                        friday.append({
                            'id': data['id'],
                            'hour': data['hour'],
                            'minute': data['minute'],
                        })
                        day_check['friday'] = True
                    if data['saturday']:
                        saturday.append({
                            'id': data['id'],
                            'hour': data['hour'],
                            'minute': data['minute'],
                        })
                        day_check['saturday'] = True

            days_time['sunday'] = sunday
            days_time['monday'] = monday
            days_time['tuesday'] = tuesday
            days_time['wednesday'] = wednesday
            days_time['thursday'] = thursday
            days_time['friday'] = friday
            days_time['saturday'] = saturday

            flagValues.unsetAlarmFlag()

        now = datetime.now()
        today = now.strftime("%A").lower()

        # Check if alarm is set for todays day
        if(day_check[today]):
            time_hour = int(now.strftime("%H"))
            time_minute = int(now.strftime("%M"))
            time_second = int(now.strftime("%S"))

            # alarm_split = alarmTime.split(":")

            # print(str(time_second) + '------------------++++++' + str(alarm_split[1]))

            for alarm_data in days_time[today]:
                if(time_hour == alarm_data['hour'] and time_minute == alarm_data['minute'] and time_second < 10):
                    print('-------------')
                    p = multiprocessing.Process(target=playsound, args=("./sounds/alarmSoundLove.mp3",))
                    p.start()
                    time.sleep(5)
                    p.terminate()
                # else:
                #     print("alarm is not active")

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