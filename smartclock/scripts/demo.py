import json
import requests
import flagValues


# alarmFlagJson = open('alarmFlag.json')
# alarmFlag = json.load(alarmFlagJson)

# print(alarmFlag['alarm_flag'])

# flagValues.unsetAlarmFlag()

x = requests.get('http://192.168.1.9:8000/api/alarm').json()

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
    # print('------------')

days_time['sunday'] = sunday
days_time['monday'] = monday
days_time['tuesday'] = tuesday
days_time['wednesday'] = wednesday
days_time['thursday'] = thursday
days_time['friday'] = friday
days_time['saturday'] = saturday

# print(days_time['monday'])

if day_check['monday']:
    # print('test')
    for alarm_data in days_time['monday']:
        print(alarm_data['hour'])
        print('------------')
