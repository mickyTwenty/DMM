import time
import threading
from Config import _App
from Config import APP_STATE

class AppcheckerThread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI

    def run(self):
        print('Entering Into App State Checker Thread')

        while _App.CHECKERSTAT:
            print("App State Checking")
            if _App._Settings.TRUCK_ID == '':
                _App.APPSTATE = APP_STATE.STATE_NEED_TRUCKID
            elif _App.LoginState is False:
                _App.APPSTATE = APP_STATE.STATE_NEED_LOGIN
            else:
                _App.APPSTATE = APP_STATE.STATE_BEGIN_LIFT
            
            self.GUI.setAppState()


            time.sleep(1)

        print('Exiting From App State Checker Thread')