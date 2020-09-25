import time
import threading
import requests
import json

from Config import _App
from Config import APP_STATE
from DBHelper import _DB



class APICallThread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI

    def run(self):
        print('Entering Into API CALL Thread')

        while _App.APICALLSTAT:

            if len(self.GUI.message_queue) > 0:

                LID = self.GUI.message_queue[0]
                FB = self.GUI.message_queue[1]

                res = self.send_request(FB)
                print("res1: ", res)
                print("res1 type:", type(res))

                if res is False:
                    self.GUI.setAPICallLog(LID + "\tFailed")
                else:
                    if res["IsSuccess"] is True:
                        self.GUI.setAPICallLog(LID + "\tOK")
                    else:
                        self.GUI.setAPICallLog(LID + "\t{}".format(data["ErrorMessage"]))



                self.GUI.message_mutex.lock()

                self.GUI.message_queue.pop(0)
                self.GUI.message_queue.pop(0)

                self.GUI.message_mutex.unlock()


            time.sleep(1)

        print('Exiting From API CALL Thread')

    def send_request(self, data):
        url = "http://{}/api/FreightBillWeight".format(_App._Settings.CLIENT_HOST)

        json_data = dict(zip(["Barcodes", "ForkliftId", "Weight", "UOM", "ActiveUser", "ScanTime"], data))

        if _App.DEBUG == False:
            res = [
                {'IsSuccess': True, 'FreightBill': 'F2470280', 'ErrorMessage': None, 'WeightApplication': 2},
                {'IsSuccess': False, 'FreightBill': 'F2470285', 'ErrorMessage': 'Deferring update, not all barcodes for bill have been submitted.', 'WeightApplication': 3},
                {'IsSuccess': False, 'FreightBill': None, 'ErrorMessage': "Couldn't find specified barcode.", 'WeightApplication': 0},
                {"IsSuccess": True, "BillNumber": "T00001", "WeightApplication": 1}
            ]
        else:
            status = 0
            try_no = 0
            status = 0
            response = None
            while status != 200 and status != 400 and try_no < 3:
                try:
                    response = requests.post(url, data = json_data)
                    status = response.status_code

                    print('Status code: ', response.status_code)
                    print(response.json())
                except requests.exceptions.RequestException as e:
                    print(e)
                    break
                finally:
                    try_no += 1
                    
                
            
            if status != 200 and status != 400:
                return False
            
            return response.json()