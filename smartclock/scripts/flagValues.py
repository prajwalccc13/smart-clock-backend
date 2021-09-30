import json

"""
Flag for alarm
"""


def setAlarmFlag():
    flags = {
        "alarm_flag": True,
    }
    json_object = json.dumps(flags, indent = 4)
    with open("alarmFlag.json", "w") as outfile:
        outfile.write(json_object)

def unsetAlarmFlag():
    flags = {
        "alarm_flag": False,
    }
    json_object = json.dumps(flags, indent = 4)
    with open("alarmFlag.json", "w") as outfile:
        outfile.write(json_object)



"""
Flag for routines
"""

routine_flag = False

def setRoutineFlag():
    flags = {
        "routine_flag": True,
    }
    json_object = json.dumps(flags, indent = 4)
    with open("routineFlag.json", "w") as outfile:
        outfile.write(json_object)

def unsetRoutineFlag():
    flags = {
        "routine_flag": False,
    }
    json_object = json.dumps(flags, indent = 4)
    with open("routineFlag.json", "w") as outfile:
        outfile.write(json_object)


unsetRoutineFlag()