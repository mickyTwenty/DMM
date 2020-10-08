from PyQt5.QtCore import QMutex
import sqlite3
from sqlite3 import Error

global _DB

db_file = "./res/db/weightrpi.db"

'''
RES_CODE
    0~3 : Scenario0 ~ 3
    4   : The request is invalid
    5   : Ignored Request(No FB Items)
'''

class DBHelper():
    def __init__(self):
        self.mutex = QMutex()

        try:
            print("DB Connecting...")
            self.conn = sqlite3.connect(db_file)
            print("DB Connected: ", db_file)

        except Error as e:
            print(e)
    
    def closeDB(self):
        print("DB Closing...")
        self.conn.commit()
        self.conn.close()

    def insertNewLift(self, data):
        try:
            self.mutex.lock()
            cur = self.conn.cursor()

            cur.execute("INSERT INTO tbl_lift_info(truck_id, lift_id, fb_id, lift_weight, uom, user_id, transaction_id, datetime) VALUES (?,?,?,?,?,?,?,?)", data)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            self.mutex.unlock()

    def setIgnoreLift(self, LID):
        try:
            self.mutex.lock()
            cur = self.conn.cursor()

            cur.execute("UPDATE tbl_lift_info SET res_success=:SUCCESS, res_message=:MESSAGE, res_code=:CODE WHERE lift_id=:LID", {"SUCCESS": str(False), "MESSAGE": "Ignored request(No FB Items)", "CODE": 5, "LID": LID})
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            self.mutex.unlock()
    
    def setFBId(self, LID, FBID):
        try:
            self.mutex.lock()
            cur = self.conn.cursor()

            cur.execute("UPDATE tbl_lift_info SET fb_id=:FBID WHERE lift_id=:LID", {"FBID": FBID, "LID": LID})
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            self.mutex.unlock()

    def setLiftTransaction(self, LID, data):
        lift = []
        try:
            self.mutex.lock()
            cur = self.conn.cursor()

            if data == False:
                cur.execute("UPDATE tbl_lift_info SET res_success=:SUCCESS, res_message=:MESSAGE, res_code=:CODE WHERE lift_id=:LID", {"SUCCESS": str(False), "MESSAGE": "Connection Problem", "CODE": 404, "LID": LID})
            elif data["WeightApplication"] == 4:
                cur.execute("UPDATE tbl_lift_info SET res_success=:SUCCESS, res_message=:MESSAGE, res_code=:CODE WHERE lift_id=:LID", {"SUCCESS": str(data["IsSuccess"]), "MESSAGE": data["Message"], "CODE": data["WeightApplication"], "LID": LID})
            else:
                cur.execute("UPDATE tbl_lift_info SET res_success=:SUCCESS, res_message=:MESSAGE, res_code=:CODE WHERE lift_id=:LID", {"SUCCESS": str(data["IsSuccess"]), "MESSAGE": data["ErrorMessage"], "CODE": data["WeightApplication"], "LID": LID})

            cur.execute("SELECT * FROM tbl_lift_info WHERE lift_id=:LID", {"LID": LID})
            row = cur.fetchone()

            lift.append(row[3])
            lift.append(row[11])


        except Error as e:
            print(e)
        finally:
            self.mutex.unlock()

        return lift

    def insertNewFBItem(self, data):
        is_new = False

        try:
            self.mutex.lock()
            cur = self.conn.cursor()

            cur.execute("SELECT COUNT(*) FROM tbl_fb_items WHERE lift_id=:LID AND fb_item_barcode=:BARCODE", {"LID": data[0], "BARCODE": data[2]})
            exist_one = cur.fetchone()

            if exist_one[0] == 0:
                is_new = True
                cur.execute("INSERT INTO tbl_fb_items(lift_id, scan_id, fb_item_barcode, datetime) VALUES (?,?,?,?)", data)
                self.conn.commit()

        except Error as e:
            print(e)
        finally:
            self.mutex.unlock()
            return is_new


    def getFBItems(self, LID):
        data = []

        try:
            self.mutex.lock()
            cur = self.conn.cursor()

            cur.execute("SELECT fb_item_barcode FROM tbl_fb_items WHERE lift_id=:LID ORDER BY fb_item_barcode", {"LID": LID})
            rs = cur.fetchall()
           
            items = []
            for row in rs:
                items.append(row[0])

            data.append(items)

            cur.execute("SELECT truck_id, lift_weight, uom, user_id, transaction_id, datetime FROM tbl_lift_info WHERE lift_id=:LID", {"LID": LID})
            rs = cur.fetchone()

            data += rs

        except Error as e:
            print(e)
        finally:
            self.mutex.unlock()
            return data

        return data

    def getPendingLift(self):
        pending_lift = None
        try:
            self.mutex.lock()
            cur = self.conn.cursor()

            cur.execute("SELECT lift_id FROM tbl_lift_info WHERE res_code = 404 OR res_code IS NULL ORDER BY lift_id ASC")
            rs = cur.fetchone()

            if rs is not None:
                pending_lift = rs[0]

        except Error as e:
            print(e)
        finally:
            self.mutex.unlock()
        
        return pending_lift

    


_DB = DBHelper()