from BarcodeScannerThread import BarcodeScannerThread

class BarcodeScannerHelper:
    def __init__(self, GUI):
        self.GUI = GUI
        self.t = BarcodeScannerThread(self.GUI)

    def startScan(self):
        self.t.start()

    def stopScan(self):
        self.t.raise_exception()
        self.t.join()
        if not self.t.isAlive():
            print('Barcode Scanner Thread killed.')
