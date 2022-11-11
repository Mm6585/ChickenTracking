import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('./key/Firebase_Realtime_DB_key.json')  # 키 변경

firebase_admin.initialize_app(cred, {
    'databaseURL': 'Firebase_Realtime_DB_url'    # URL 변경
})

ref = db.reference('/')
users = ref.child('Users')
tracks = ref.child('Tracking')

def get_users_data():
    users_dict = users.get()
    if (users_dict != None):
        return users_dict
    else:
        return {}

def is_user(users_dict, id):
    if (id in users_dict):
        return True
    return False

def add_user(user_name, user_email):
    users.child(user_name).child('email').set(user_email)

def get_tracking_data():
    tracking_data = tracks.get()
    if (tracking_data != None):
        return tracking_data
    else:
        return {}
