import time
import threading
from datetime import datetime
from Config import _App


class ClockTimeThread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI
        self.OLDTIME = ''

    def run(self):
        while _App.TIMESTAT:
            now = datetime.now()
            currentTime = now.strftime("%H:%M %p")
            currentDate = now.strftime("%A, %B %d, %Y")
            timestamp = currentTime + ' ' + currentDate
            if timestamp != self.OLDTIME:
                self.GUI.updateTimeText(timestamp)
                self.OLDTIME = timestamp
            time.sleep(1)