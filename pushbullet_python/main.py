from pushbullet import Pushbullet
import db

api_key = 'o.Us9crOXIPVZyMoVRVtAwGwjW6R4yeLhc'
pb = Pushbullet(api_key)

introduce = '''
Hi. I'm ChickTrack manager.

If you want to know how to use this service,
please type "!help".

If you want to contact me,
send me an e-mail to "mmj6585@gmail.com".
'''

help = '''
!subscribe
Send you notification about daily result.
!
'''

def listen_pushes():
    while(True):
        pushes = pb.get_pushes()

        for push in pushes:
            if ('body' in push):
                if ('!' not in push['body']):
                    push_first(push)
                elif ('!help' in push['body']):
                    push_help(push)
                elif (('!subscribe' in push['body']) and (push['sender_email'] != '20172608@edu.hanbat.ac.kr')):
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

if __name__ == '__main__':
    delete_pushes()
    listen_pushes()