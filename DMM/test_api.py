import requests
import json

username = "WeighPointAPI"
password = "dsfg9jsjWE0sjvm"

newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

#datas = {'Barcodes': ['F2332150'], 'ScanTime': '2020-06-24T00:00:00', 'Weight': 0.0, 'ForkliftId': 33, 'ScannerId': 0, 'ActiveUser': 'Test', 'UOM': 'LB', 'TransactionId': 0}

#datas = '{"Barcodes": ["F2332150-0001","F2332150-0002", "F2332155-0001"], "ScanTime": "2020-06-24T00:00:00", "Weight": 0.0, "ForkliftId": "33", "ScannerId": 0, "ActiveUser": "Test", "UOM": "LB", "TransactionId": 0}'

#datas = '{"Barcodes": ["F2470286-0001", "F2470286-0002", "F2470286-0003", "F2470286-0004", "F2470286-0005"], "ScanTime": "2020-06-24T00:00:00", "Weight": 100.0, "ForkliftId": "33", "ScannerId": 0, "ActiveUser": "Test", "UOM": "LB", "TransactionId": 0}'

#datas = '{"Barcodes": ["F2470280-0001", "F2470280-0002"], "ScanTime": "2020-06-24T00:00:00", "Weight": 100.0, "ForkliftId": "33", "ScannerId": 0, "ActiveUser": "Test", "UOM": "LB", "TransactionId": "TRANS-TRUCK1-20200925"}'

#datas = '{"Barcodes": ["F2470285-0001"], "ScanTime": "2020-06-24T00:00:00", "Weight": 100.0, "ForkliftId": "33", "ScannerId": 0, "ActiveUser": "Test", "UOM": "LB", "TransactionId": 0}'

#datas = '{"Barcodes": ["F2470280-0001", "F2470280-0002"], "ScanTime": "2020-06-24T00:00:00", "Weight": 100.0, "ForkliftId": "33", "ActiveUser": "Test", "UOM": "LB"}'



#datas = '{"Barcodes": ["F2332150"], "ScanTime": "2020-06-24T00:00:00", "Weight": 0.0, "ForkliftId": "33", "ScannerId": 0, "ActiveUser": "Test", "UOM": "LB", "TransactionId": 0}'

datas = '{"Barcodes": ["F2332150-0001"], "ScanTime": "2020-06-24T00:00:00", "Weight": 0.0, "ForkliftId": "33", "ScannerId": 0, "ActiveUser": "Test", "UOM": "LB", "TransactionId": 0}'

datas = '{"Barcodes": ["111111"],"ScanTime": "2020-06-24T00:00:00","Weight": 0.0,"ForkliftId": "33","ScannerId": 0,"ActiveUser": "Test","UOM": "LB","TransactionId": 0}'

datas = '{"Barcodes": ["F2332150-0001","F2332150-0002"],"ScanTime": "2020-06-24T00:00:00","Weight": 0.0,"ForkliftId": "33","ScannerId": 0,"ActiveUser": "Test","UOM": "LB","TransactionId": 0}'

datas = '{"Barcodes": ["F2332150-0001","F2332150-0002"],"ScanTime": "2020-06-24T00:00:00","Weight": 0.0,"ScannerId": 0,"ActiveUser": "Test","UOM": "LB","TransactionId": 0}'

datas = '{"Barcodes": ["F2332150-0001","F2332150-0002"],"ScanTime": "2020-06-24T00:00:00","Weight": 0.0,"ForkliftId": "33","ScannerId": 0,"ActiveUser": "Test","TransactionId": 0}'

datas = '{"Barcodes": ["F2332150-0001","F2332149-0002"],"ScanTime": "2020-06-24T00:00:00","Weight": 0.0,"ForkliftId": "33","ScannerId": 0,"ActiveUser": "Test","UOM": "LB","TransactionId": 0}'


#response = requests.post('http://10.0.0.250/api/FreightBillWeight', json=json.loads(datas), auth=(username, password), headers = newHeaders)

response = requests.post('http://10.0.0.250/api/FreightBillWeight', json=json.loads(datas))

print('Status code: ', response.status_code)
print(response.json())
