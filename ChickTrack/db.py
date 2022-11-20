# pip install firebase_admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
from measure_dist import measure_dist

class DB:
    def __init__(self, user_id):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('/Users/kimgyujin/Desktop/ChickenTracking/ChickTrack/key/Firebase_Realtime_Database_key.json')  # 키 변경

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://chicktrack-4ee59-default-rtdb.firebaseio.com/'    # URL 변경
        })

        # As an admin, the app has access to read and write all data, regradless of Security Rules
        self.ref = db.reference('/Tracking/' + user_id)
        self.today = str(datetime.today()).split()[0].replace('-', '')

    def is_prev_None(self):
        prev_data = self.ref.child(self.today).get()
        if (prev_data != None):
            # del prev_data
            del prev_data['aoa']
            if (len(prev_data) == 0):
                return True, None
            else:
                return False, prev_data
        else:
            return True, None

    def cal_aoa(self, cur_data, is_prev_none, prev_data):
        aoa = 0

        if (is_prev_none):
            return 0
        else:
            for id in cur_data:
                if (id in prev_data):
                    x1, y1, box1 = prev_data[id]['x'], \
                                    prev_data[id]['y'], \
                                    prev_data[id]['box']
                    x2, y2, box2 = cur_data[id]['x'], \
                                    cur_data[id]['y'], \
                                    cur_data[id]['box']
                    aoa += measure_dist(x1, y1, x2, y2, box1, box2)            
        return aoa

    def update_db(self, data):
        is_prev_none, prev_data = self.is_prev_None()

        aoa = self.cal_aoa(data, is_prev_none, prev_data)
        prev_aoa = self.ref.child(self.today).child('aoa').get()
        if (prev_aoa == None):
            prev_aoa = 0
        aoa += prev_aoa

        if (is_prev_none):
            self.ref.child(self.today).set(data)
        else:
            
            self.ref.child(self.today).update(data)
        self.ref.child(self.today).child('aoa').set(aoa)
        
    def  del_db(self):
        data = self.ref.child(self.today)
        data.delete()
        
        

    def cal_avg_aoa(self):
        data = self.ref.child(self.today).get()
        aoa = data['aoa']
        n = len(data) - 1
        self.ref.child(self.today).child('aoa').set(aoa/n)

    def get_scaling_data(self, period):
        days = self.ref.get()[:-period]
        aoa_list = list()

        for day in days:
            aoa_list.append(self.ref.child(day).child('aoa').get())

        scaling_data = [((i-min(aoa_list))/(max(aoa_list)-min(aoa_list))+0.01) for i in aoa_list]

        return scaling_data
