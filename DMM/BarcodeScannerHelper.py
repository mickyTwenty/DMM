from BarcodeScannerThread import BarcodeScannerThread

class BarcodeScannerHelper:
    def __init__(self, GUI):
        self.GUI = GUI

    def startScan(self):
        BarcodeScannerThread(self.GUI).start()