from PyQt5.QtCore import QMutex
import sqlite3
from sqlite3 import Error

global _DB

db_file = "./res/db/weightrpi.db"

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

            cur.execute("INSERT INTO tbl_lift_info(truck_id, lift_id, fb_id, lift_weight, uom, user_id, datetime) VALUES (?,?,?,?,?,?,?)", data)
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

            cur.execute("SELECT truck_id, lift_weight, uom, user_id, datetime FROM tbl_lift_info WHERE lift_id=:LID", {"LID": LID})
            rs = cur.fetchone()

            data += rs

        except Error as e:
            print(e)
        finally:
            self.mutex.unlock()
            return data

        return data


    


_DB = DBHelper()