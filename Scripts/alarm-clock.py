from datetime import date, datetime
import time
import subprocess
import multiprocessing

from playsound import playsound


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

def alarm(AlarmTime, AlarmDays):
    while True:
        now = datetime.now()
        today = now.strftime("%A").lower()

        # Check if alarm is set for todays day
        if(AlarmDays[today]):
            time_hour = int(now.strftime("%H"))
            time_minute = int(now.strftime("%M"))
            time_second = int(now.strftime("%S"))

            alarm_split = alarmTime.split(":")

            # print(str(time_second) + '------------------++++++' + str(alarm_split[1]))

            if(time_hour == alarm_split[0] and time_minute == alarm_split[1] and time_second < 10):
                p = multiprocessing.Process(target=playsound, args=("./sounds/alarmSoundLove.mp3",))
                p.start()
                time.sleep(5)
                p.terminate()
            else:
                print("alarm is not active")

            time.sleep(1)

days = {
    'sunday': True,
    'monday': True,
    'tuesday': True,
    'wednesday': True,
    'thursday': True,
    'friday': True,
    'saturday': True,
}
alarmTime = "23:30"
alarm(alarmTime, days)