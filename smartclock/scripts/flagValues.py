import json

"""
Flag for alarm
"""


def setAlarmFlag():
    flags = {
        "alarm_flag": True,
    }
    json_object = json.dumps(flags, indent = 4)
    with open("smartclock/scripts/alarmFlag.json", "w") as outfile:
        outfile.write(json_object)
        print("from models")

def unsetAlarmFlag():
    flags = {
        "alarm_flag": False,
    }
    json_object = json.dumps(flags, indent = 4)
    with open("smartclock/scripts/alarmFlag.json", "w") as outfile:
        outfile.write(json_object)



"""
Flag for routines
"""

def setRoutineFlag():
    flags = {
        "routine_flag": True,
    }
    json_object = json.dumps(flags, indent = 4)
    with open("smartclock/scripts/routineFlag.json", "w") as outfile:
        outfile.write(json_object)

def unsetRoutineFlag():
    flags = {
        "routine_flag": False,
    }
    json_object = json.dumps(flags, indent = 4)
    with open("smartclock/scripts/routineFlag.json", "w") as outfile:
        outfile.write(json_object)
