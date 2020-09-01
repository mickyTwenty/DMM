import time
import threading
from Config import _App

from wireless import Wireless


class WirelessThread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI
        self.wireless = Wireless()

    def run(self):
        while _App.WIFISTAT:
            print(self.wireless.current)
            if ( self.wireless.current() is not None):
                print("wifi connected")
                _App.WIFI_CONNECTION = True
            else:
                print("wifi connection is none")
                _App.WIFI_CONNECTION = False
            time.sleep(10)