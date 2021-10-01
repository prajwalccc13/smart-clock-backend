import flagValues
import json


# flagValues.setAlarmFlag()
# alarmFlagJson = open('alarmFlag.json')
# alarmFlag = json.load(alarmFlagJson)
# print('After set Alarm Flag - ' + str(alarmFlag['alarm_flag']))

flagValues.unsetAlarmFlag()
alarmFlagJson = open('alarmFlag.json')
alarmFlag = json.load(alarmFlagJson)
print('After unset Alarm Flag - ' + str(alarmFlag['alarm_flag']))

# flagValues.setRoutineFlag()
# routineFlagJson = open('routineFlag.json')
# routineFlag = json.load(routineFlagJson)
# print('After set Routine Flag' + str(routineFlag['routine_flag']))



# flagValues.unsetRoutineFlag()
# routineFlagJson = open('routineFlag.json')
# routineFlag = json.load(routineFlagJson)
# print('After unset Routine Flag' + str(routineFlag['routine_flag']))