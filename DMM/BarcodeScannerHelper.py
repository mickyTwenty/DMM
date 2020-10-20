from BarcodeScannerThread import BarcodeScannerThread

class BarcodeScannerHelper:
    def __init__(self, GUI):
        self.GUI = GUI
        self.t = BarcodeScannerThread(self.GUI)

    def startScan(self):
        self.t.start()

    def stopScan(self):
        print('a')
        self.t.raise_exception()
        print('b')
        self.t.join()
        print('c')
        if not self.t.isAlive():
            print('d')
            print('Barcode Scanner Thread killed.')
            print('e')
        print('f')
