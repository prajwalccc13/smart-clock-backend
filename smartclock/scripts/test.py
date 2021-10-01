import multiprocessing
import time

from pydub import AudioSegment
from pydub.playback import play

# p = multiprocessing.Process(target=AudioSegment.from_mp3, args=("./sounds/alarmSoundLove.mp3",))
# p.start()
# time.sleep(5)
# p.terminate()

song = AudioSegment.from_mp3("./sounds/alarmSoundLove.mp3")
play(song)