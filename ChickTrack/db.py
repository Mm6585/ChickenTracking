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

    def get_prev_data(self, id):
        data = self.ref.child(self.today).child(str(id)).get()
        if (data == None):
            x1 = 0
            y1 = 0
            box1 = 0
        else:
            x1 = data['x']
            y1 = data['y']
            box1 = data['box']
        return x1, y1, box1

    def cal_aoa(self, id, x2, y2, box2):
        x1, y1, box1 = self.get_prev_data(str(id))
        if (box1 != 0):
            aoa = self.ref.child(self.today).child('aoa').get()
            aoa += measure_dist(x1, y1, x2, y2, box1, box2)
        else:
            aoa = self.ref.child(self.today).child('aoa').get()
            if (aoa == None):
                aoa = 0
        
        return aoa

    def update_db(self, id, x2, y2, box2):
        aoa = self.cal_aoa(id, x2, y2, box2)
        data = {
            'x': x2,
            'y': y2,
            'box': box2,
        }
        self.ref.child(self.today).child(str(id)).set(data)
        self.ref.child(self.today).child('aoa').set(aoa)

    def cal_avg_aoa(self):
        aoa = self.ref.child(self.today).child('aoa').get()
        n = len(self.ref.get()) - 1
        self.ref.child(self.today).child('aoa').set(aoa/n)

    def get_scaling_data(self, period):
        days = self.ref.get()[:-period]
        aoa_list = list()

        for day in days:
            aoa_list.append(self.ref.child(day).child('aoa').get())

        scaling_data = [((i-min(aoa_list))/(max(aoa_list)-min(aoa_list))+0.01) for i in aoa_list]

        return scaling_data