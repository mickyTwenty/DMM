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
            if ( self.wireless.current() is not None):
                print("wifi connected...")
            else:
                print("wifi connection is none.")
            time.sleep(1)