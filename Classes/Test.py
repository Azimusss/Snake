from utilities import *
import threading
import time

# play_music('JT_Machinima.mp3')


class ClockThread(threading.Thread):
    def __init__(self,interval):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.interval)
t = ClockThread(15)
t.start()
