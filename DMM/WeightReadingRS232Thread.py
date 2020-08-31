import threading
import sqlite3
import re
import time
import decimal
from barcode.writer import ImageWriter
import barcode
from sqlite3 import Error
from datetime import datetime
from SerialConfig import SerialConfig
import qrcode
from PIL import Image
import numpy as np
import random
from RS232Serial import RS232Serial
from Config import _App

class WeightReadingRs232Thread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI
        self.OLDWEIGHT = '0'

    def decodeSerialRes(self, res):
        try:
            print("read data: " + res)
            response = re.sub(r"[^a-zA-Z0-9]+", ' ', res)
            response = response.strip()
        except:
            response = ''
        finally:
            return response

    def initSerial(self):
        self.rs232 = RS232Serial()
        stat = self.rs232.checkSerial()
        self.rsserial = self.rs232.ser
        return stat

    def run(self):
        print('Entering Into RS232 Thread')
        
        if _App.DEBUG is False and not self.initSerial():
            return

        while _App.RS232STAT:
            if _App.DEBUG is True:
                ############ TESTING
                cval = random.randint(0, 1)
                mval = random.randint(0, 1)
                rval = random.randint(5000, 10000) * 1.7

                if cval == 0:
                    response = str(rval) + ' LBS GR'
                else:
                    response = str(rval) + ' KG GR'

                if mval == 1:
                    response += ' M'

                print("received data: " + response)
                weight = self.extractDigit(response)
                if weight != '-1':
                    self.doProcessing(response, weight)
                # time.sleep(self.window.INTERVAL)
                time.sleep(1)
            else:
                if self.rsserial.isOpen():
                    self.rsserial.flushInput()
                    self.rsserial.flushOutput()
                    #time.sleep(0.5)
                try:
                    if self.rsserial.isOpen():
                        response = self.rsserial.readline()
                        if len(response) > 5:
                            response = self.rsserial.readline().decode('UTF-8')
                            # response = self.rsserial.readline().decode('UTF-8')
                            # print("read data: " + response)
                            response = re.sub(r"[^a-zA-Z0-9]+", ' ', response)
                            response = response.strip()
                            print("received data: " + response)
                            if len(response) > 0:
                                currentWeight = self.extractDigit(response)
                                if currentWeight != '-1':
                                    self.doProcessing(response, currentWeight)
                                else:
                                    print('Weight coming Zero')
                        time.sleep(self.rs232.INTERVAL)
                        #self.rsserial.flushInput()
                        #self.rsserial.flushOutput()

                except Exception as e:
                    print('RS232 Serial Read Error:', e)
                    time.sleep(0.1)

        print('Exiting From RS232 Thread')

    def extractDigit(self, response):
        try:
            value = (float)(re.findall(r"[-+]?\d*\.\d+|\d+", response)[0])
            # print(response)
            value = "{0:.4f}".format(value)
            value = self.dropzeros(value)
        except:
            value = -1
            print('Weight conversion error')
        finally:
            return str(value)

    def dropzeros(self, number):
        mynum = decimal.Decimal(number).normalize()
        return mynum.__trunc__() if not mynum % 1 else float(mynum)

    def weightConversion(self, weight):
        if _App._Settings.WEIGHTMODE == 'KG':
            weight = float(weight) * 2.20462
            weight = round(weight, 1)
            weight = str(weight)
        return weight

    def doProcessing(self, response, weight):
        #weight = self.weightConversion(weight)
        try:
            if 'M' not in response and weight != self.OLDWEIGHT:
                self.OLDWEIGHT = weight

                if 'KG' in response:
                    _App._Settings.WEIGHTMODE = 'KG'
                elif 'LBS' in response:
                    _App._Settings.WEIGHTMODE = 'LBS'
                    
                print("weight: " + weight + _App._Settings.WEIGHTMODE)

                EAN = barcode.get_barcode_class('code128')
                ean = EAN(weight, writer=ImageWriter())
                fullname = ean.save('./res/img/barcode')

                if _App._Settings.WEIGHTMODE == 'KG':
                    fimg = Image.open("./res/img/kg.jpg")
                else:
                    fimg = Image.open("./res/img/lbs.jpg")
                bar = Image.open("./res/img/barcode.png")
                basewidth, height = bar.size
                # wpercent = (basewidth / float(fimg.size[0]))
                # hsize = int((float(fimg.size[1]) * float(wpercent)))
                fimg = fimg.resize((basewidth, 50), Image.ANTIALIAS)
                img_merge = np.vstack((np.asarray(bar), np.asarray(fimg)))
                img_merge = Image.fromarray(img_merge)
                barimg = img_merge.resize((240, 160), Image.ANTIALIAS)
                #barimg.save('./res/img/barcode_resized.jpg')

                qr = qrcode.QRCode(version=1,
                                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                                    box_size=50,
                                    border=1,)
                qr.add_data(weight + ' ' + _App._Settings.WEIGHTMODE)
                qr.make(fit=True)
                qrimg = qr.make_image(fill_color="black", back_color="white")
                #qrimg.save('./res/img/qrcode.png')
                #qrimg = Image.open("./res/img/qrcode.png")
                qrimg = qrimg.resize((160, 160), Image.ANTIALIAS)
                #qrimg.save('./res/img/qrcode_resized.jpg')

                self.GUI.CURRENTWEIGHT = weight
                self.GUI.updateWeightText(weight, _App._Settings.WEIGHTMODE)
                if _App._Settings.WEIGHTCODE == 'BARCODE':
                    self.GUI.updateBarCodeImage(barimg)
                elif _App._Settings.WEIGHTCODE == 'QRCODE':
                    self.GUI.updateQrCodeImage(qrimg)

            else:
                print('Response contains M')

        except Exception as e:
            print('Data Processing Error:',e)