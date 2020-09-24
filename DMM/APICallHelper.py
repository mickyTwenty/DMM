import time
import threading
from Config import _App
from Config import APP_STATE

class APICallThread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI

    def run(self):
        print('Entering Into API CALL Thread')

        while _App.APICALLSTAT:

            if len(self.GUI.message_queue) > 0:
                LID = self.GUI.message_queue[0]

                self.GUI.setAPICallLog(LID)
                self.GUI.message_queue.pop(0)


            time.sleep(1)

        print('Exiting From API CALL Thread')