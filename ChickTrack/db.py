# pip install firebase_admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
from measure_dist import measure_dist

class DB:
    def __init__(self, user_id):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('./key/chicktrack-4ee59-firebase-adminsdk-1x60r-b6e29c727c.json')  # 키 변경

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://chicktrack-4ee59-default-rtdb.firebaseio.com/'    # URL 변경
        })

        # As an admin, the app has access to read and write all data, regradless of Security Rules
        self.ref = db.reference('/' + user_id)
        self.today = str(datetime.today()).split()[0].replace('-', '')

    def get_prev_coor(self, id, c):
        return self.ref.child(self.today).child(str(id)).child(c).get()

    def cal_aoa(self, id, x2, y2):
        aoa = 0
        x1 = self.get_prev_coor(str(id), 'x')
        if (x1 != None):
            y1 = self.get_prev_coor(str(id), 'y')
            aoa = self.ref.child(self.today).child('aoa').get()
            aoa += measure_dist(x1, y1, x2, y2)
        else:
            aoa = self.ref.child(self.today).child('aoa').get()
        
        return aoa

    def update_db(self, id, x2, y2):
        aoa = self.cal_aoa(id, x2, y2)
        self.ref.child(self.today).child(str(id)).child('x').set(x2)
        self.ref.child(self.today).child(str(id)).child('y').set(y2)
        self.ref.child(self.today).child('aoa').set(aoa)

    def init_aoa(self):
        days = self.ref.child('aoa').get()
        if (days[-1] != self.today):
            self.ref.child('aoa').child(self.today).set(0)

    def cal_avg_aoa(self):
        aoa = self.ref.child('aoa').child(self.today).get()
        n = len(self.ref.get()) - 1
        self.ref.child('aoa').child(self.today).set(aoa/n)