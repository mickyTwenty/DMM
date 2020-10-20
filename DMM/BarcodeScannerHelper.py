from BarcodeScannerThread import BarcodeScannerThread

class BarcodeScannerHelper:
    def __init__(self, GUI):
        self.GUI = GUI
        self.t = BarcodeScannerThread(self.GUI)

    def startScan(self):
        self.t.start()

    def stopScan(self):
        if not self.t.isAlive():
            print('Barcode Scanner Thread killed.')
