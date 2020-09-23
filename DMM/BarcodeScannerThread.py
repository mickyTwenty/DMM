import sys
import threading
import time

from Config import _App
from Config import APP_STATE

class BarcodeScannerThread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI

        if _App.DEBUG is False:
            self.fp = open("/dev/hidraw2", "rb")

    def run(self):
        print("Entering Barcode Scan Thread")

        while _App.BCSCANSTAT:
            if _App.APPSTATE != APP_STATE.STATE_SCAN_BARCODE:
                time.sleep(1)
                continue

            print("Scan Barcode")

            if _App.DEBUG is True:
                print("Debug")
            else:
                print("Scan")

            time.sleep(0.5)

        if _App.DEBUG is False:
            self.fp.close()

        print("Exiting Barcode Scan Thread")