
import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes
import evdev
import time
import threading
from time import perf_counter

global BARCODE
BARCODE = 'ERROR'


class IRScanner():
    def __init__(self):
        self.BCMPIN_SCAN = 17

        self.CODE_MAP_CHAR = {
            'KEY_MINUS': "-",
            'KEY_SPACE': " ",
            'KEY_U': "U",
            'KEY_W': "W",
            'KEY_BACKSLASH': "\\",
            'KEY_GRAVE': "`",
            'KEY_NUMERIC_STAR': "*",
            'KEY_NUMERIC_3': "3",
            'KEY_NUMERIC_2': "2",
            'KEY_NUMERIC_5': "5",
            'KEY_NUMERIC_4': "4",
            'KEY_NUMERIC_7': "7",
            'KEY_NUMERIC_6': "6",
            'KEY_NUMERIC_9': "9",
            'KEY_NUMERIC_8': "8",
            'KEY_NUMERIC_1': "1",
            'KEY_NUMERIC_0': "0",
            'KEY_E': "E",
            'KEY_D': "D",
            'KEY_G': "G",
            'KEY_F': "F",
            'KEY_A': "A",
            'KEY_C': "C",
            'KEY_B': "B",
            'KEY_M': "M",
            'KEY_L': "L",
            'KEY_O': "O",
            'KEY_N': "N",
            'KEY_I': "I",
            'KEY_H': "H",
            'KEY_K': "K",
            'KEY_J': "J",
            'KEY_Q': "Q",
            'KEY_P': "P",
            'KEY_S': "S",
            'KEY_X': "X",
            'KEY_Z': "Z",
            'KEY_KP4': "4",
            'KEY_KP5': "5",
            'KEY_KP6': "6",
            'KEY_KP7': "7",
            'KEY_KP0': "0",
            'KEY_KP1': "1",
            'KEY_KP2': "2",
            'KEY_KP3': "3",
            'KEY_KP8': "8",
            'KEY_KP9': "9",
            'KEY_5': "5",
            'KEY_4': "4",
            'KEY_7': "7",
            'KEY_6': "6",
            'KEY_1': "1",
            'KEY_0': "0",
            'KEY_3': "3",
            'KEY_2': "2",
            'KEY_9': "9",
            'KEY_8': "8",
            'KEY_LEFTBRACE': "[",
            'KEY_RIGHTBRACE': "]",
            'KEY_COMMA': ",",
            'KEY_EQUAL': "=",
            'KEY_SEMICOLON': ";",
            'KEY_APOSTROPHE': "'",
            'KEY_T': "T",
            'KEY_V': "V",
            'KEY_R': "R",
            'KEY_Y': "Y",
            'KEY_TAB': "\t",
            'KEY_DOT': ".",
            'KEY_SLASH': "/",
            'KEY_LEFTSHIFT': "",
            'KEY_KEYBOARD': ""
        }

    def parse_key_to_char(self, val):
        return self.CODE_MAP_CHAR[val] if val in self.CODE_MAP_CHAR else "$"

    def openConnection(self):
        print('Start GPIO')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BCMPIN_SCAN, GPIO.OUT)
        GPIO.output(self.BCMPIN_SCAN, GPIO.HIGH)
        try:
            GPIO.output(self.BCMPIN_SCAN, GPIO.LOW)
            time.sleep(3)

            GPIO.output(self.BCMPIN_SCAN, GPIO.HIGH)
            GPIO.cleanup()

            # self.readIRBarCode()

        except KeyboardInterrupt:
            print("QUIT")
        print('Close GPIO')

    # def closeConnection(self):
    #    GPIO.output(self.BCMPIN_ON, GPIO.LOW)
    #    GPIO.output(self.BCMPIN_SCAN, GPIO.LOW)
    #    GPIO.cleanup()

    def readIRBarCode(self):
        print('Start IR')
        global BARCODE
        deviceName = 'HID 0581:020c Keyboard'
        devicePath = None
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if deviceName in device.name:
                devicePath = device.path
                break
        if devicePath != None:
            print(device.path, device.name, device.phys)
            device = InputDevice(devicePath)  # Replace with your device
            barcode = ''
            t1_start = perf_counter()
            # print(t1_start)
            # for event in device.read():
            runSTAT = True
            while runSTAT:
                try:
                    event = device.read_one()
                    t1_stop = perf_counter()
                    elapsed = t1_stop - t1_start
                    # print('Time:',elapsed)
                    if elapsed > 4:
                        break
                    if event.type == ecodes.EV_KEY:
                        eventdata = categorize(event)
                        # print(": ",eventdata.keycode)
                        # if eventdata.keystate == eventdata.key_up:  # 1 Keydown, 0 keyup
                        if eventdata.keystate == 0:  # 1 Keydown, 0 keyup
                            if eventdata.keycode == "KEY_ENTER":
                                BARCODE = barcode
                                break
                            else:
                                key = self.parse_key_to_char(eventdata.keycode)
                                barcode = barcode + key
                except:
                    continue
                    # print('')
            print('SCAN DONE:', BARCODE)
            device.close()
        print('Close IR')
        # return barcode

    def scanIRCODE(self):
        print('Init')
        global BARCODE
        x = threading.Thread(target=self.readIRBarCode, args=())
        x.start()

        y = threading.Thread(target=self.openConnection, args=())
        y.start()
        y.join()
        x.join()
        return BARCODE
# ir =IRScanner()
# ir.scanIRCODE()

