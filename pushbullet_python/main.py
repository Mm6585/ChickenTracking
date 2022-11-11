from pushbullet import Pushbullet
import db
from datetime import datetime

api_key = 'Pushbullet_API_key'
pb = Pushbullet(api_key)

introduce = '''
Hi. I'm ChickTrack manager.

If you want to know how to use this service,
please type "!help".

If you want to contact me,
send me an e-mail to "email".
'''

help = '''
Your Pushbullet name must be in english

!subscribe
Send you notification about daily result.

!
'''

def listen_pushes():
    pushed_daily_data = False

    while(True):
        now = str(datetime.now()).split(' ')[1].split('.')[0][:-3]

        if ((not pushed_daily_data) and (now == '09:00')):
            push_daily_data()
            pushed_daily_data = True
        elif(now == '00:00'):
            pushed_daily_data = False

        pushes = pb.get_pushes()

        for push in pushes:
            if ('body' in push):
                if ('!' not in push['body']):
                    push_first(push)
                elif ('!help' in push['body']):
                    push_help(push)
                elif (('!subscribe' in push['body']) and \
                    (push['sender_email'] != 'service_email')):
                    add_user(push)

        if (len(pushes) > 10):
            delete_pushes()

def push_first(push):
    user_email = push['sender_email']
    iden = push.get('iden')

    pb.push_note('', introduce, email=user_email)
    pb.delete_push(iden)

def push_help(push):
    user_name = push['sender_name']
    user_email = push['sender_email']
    iden = push.get('iden')

    pb.push_note('', help, email=user_email)
    pb.delete_push(iden)

def add_user(push):
    user_name = push['sender_name']
    user_email = push['sender_email']
    iden = push.get('iden')

    users_dict = db.get_users_data()
    if (db.is_user(users_dict, user_name)):
        pb.push_note('', 'Already subscribed', email=user_email)
        pb.delete_push(iden)
    else:
        db.add_user(user_name, user_email)
        pb.push_note('', 'Welcome to ChickTrack service!', email=user_email)
        pb.delete_push(iden)

def delete_pushes():
    pb.delete_pushes()
    pb.push_note('','',email='20172608@edu.hanbat.ac.kr')

def push_daily_data():
    users_data = db.get_users_data()
    track_data = db.get_tracking_data()
    today = str(datetime.now()).split(' ')[0].replace('-', '')

    if (len(track_data) > 0):
        for user in track_data:
            user_email = users_data[user]['email']
            today_aoa = track_data[user][today]['aoa']
            if (len(track_data) >= 7):
                week = list(track_data[user])[-7:]
            else:
                week = track_data[user]

            s = 0
            for day in week:
                s += float(week[day]['aoa'])
            m = s / len(week)
            today_ratio = today_aoa / m
            
            body = 'Average daily amount of activity : %s \
                \n\nRatio with the weekly average : %s%%' \
                % (round(today_aoa, 3), round(today_ratio, 2)*100)
            body = str(body)

            push_daily = pb.push_note(title='Daily Notification', body=body, email=user_email)

            pb.delete_push(push_daily.get('iden'))

if __name__ == '__main__':
    delete_pushes()
    listen_pushes()
