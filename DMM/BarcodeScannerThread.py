import sys
import threading
import time
import random

from Config import _App
from Config import APP_STATE

class BarcodeScannerThread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI

        if _App.DEBUG is False:
            self.fp = open("/dev/hidraw2", "rb")
        else:
            fb = open("barcodes.txt")

            self.list_barcodes = []
            self.count = 0
            for line in fb:
                bc = line.strip()
                self.list_barcodes.append(bc)
                self.count += 1

    def run(self):
        print("Entering Barcode Scan Thread")

        while _App.BCSCANSTAT:
            if _App.APPSTATE != APP_STATE.STATE_SCAN_BARCODE:
                time.sleep(1)
                continue

            print("Scan Barcode")

            if _App.DEBUG is True:
                rval = random.randint(0, self.count - 1)
                barcode_in = self.list_barcodes[rval]

                self.doProcessing(barcode_in)
                time.sleep(1)
            else:
                buffer = self.fp.read(8)
                for c in buffer:
                    if ord(c) > 0:
                        print(ord(c))
                print("\n")


        if _App.DEBUG is False:
            self.fp.close()

        print("Exiting Barcode Scan Thread")

    
    def doProcessing(self, barcode):
        self.GUI.addFBItem(barcode)