import time
import threading
import requests
import json
import random

from Config import _App
from Config import APP_STATE
from DBHelper import _DB

username = "WeighPointAPI"
password = "dsfg9jsjWE0sjvm"

newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

class APICallThread(threading.Thread):
    def __init__(self, GUI):
        threading.Thread.__init__(self)
        self.GUI = GUI

    def run(self):
        print('Entering Into API CALL Thread')

        while _App.APICALLSTAT:

            self.GUI.message_mutex.lock()
            count = len(self.GUI.message_queue)
            self.GUI.message_mutex.unlock()

            if count > 0:

                LID = self.GUI.message_queue[0]
                FB = self.GUI.message_queue[1]

                res = self.send_request(FB)
                self.GUI.newTransactionSet(LID, res)
                '''
                if res is False:
                    self.GUI.setAPICallLog(LID + "\tFailed")
                else:
                    if res["IsSuccess"] is True:
                        self.GUI.setAPICallLog(LID + "\tOK")
                    else:
                        self.GUI.setAPICallLog(LID + "\tScenario: {}".format(res["WeightApplication"]))
                '''

                self.GUI.message_mutex.lock()

                self.GUI.message_queue.pop(0)
                self.GUI.message_queue.pop(0)

                self.GUI.message_mutex.unlock()
            
            time.sleep(1)

        print('Exiting From API CALL Thread')

    def send_request(self, data):
        url = "http://{}/api/FreightBillWeight".format(_App._Settings.CLIENT_HOST)

        json_data = dict(zip(["Barcodes", "ForkliftId", "Weight", "UOM", "ActiveUser", "TransactionId", "ScanTime"], data))

        print("request data: ", json_data)

        if _App.DEBUG == True:
            res = [
                {'IsSuccess': True, 'FreightBill': 'F2470280', 'ErrorMessage': None, 'WeightApplication': 2},
                {'IsSuccess': False, 'FreightBill': 'F2470285', 'ErrorMessage': 'Deferring update, not all barcodes for bill have been submitted.', 'WeightApplication': 3},
                {'IsSuccess': False, 'FreightBill': None, 'ErrorMessage': "Couldn't find specified barcode.", 'WeightApplication': 0},
                {"IsSuccess": True, "FreightBill": "T00001", 'ErrorMessage': None, "WeightApplication": 1},
                False
            ]
            rval = random.randint(0, 4)
            response = res[rval]

            if response == False:
                return response

            if response['TransactionId'] == json_data['TransactionId']:
                response['IsSuccess'] = True
            else:
                response['IsSuccess'] = False

            return res[rval]
        else:
            status = 0
            try_no = 0
            status = 0
            response = None
            while status != 200 and status != 400 and try_no < 3:
                try:
                    response = requests.post(url, json = json_data, auth=(username, password), headers = newHeaders)
                    status = response.status_code

                    print('Status code: ', response.status_code)
                    print(response.json())

                    # Add handle invalid request

                    json_response = response.json()

                    if json_response.has_key("Message") and json_response['ErrorMessage'] == 'The request is invalid.':
                        json_response['IsSuccess'] = False
                        json_response['WeightApplication'] = 4
                        break

                    if json_response.has_key('TransactionId') and json_response['TransactionId'] != json_data['TransactionId']:
                        json_response['IsSuccess'] = False
                        json_response['ErrorMessage'] = 'TransactionID verification failed.'

                except requests.exceptions.RequestException as e:
                    print(e)
                    break
                finally:
                    try_no += 1
                    
            if status != 200 and status != 400:
                return False
            
            return json_response