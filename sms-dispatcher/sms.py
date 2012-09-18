from flask import json
import requests
from settings import MODEM, REMOTE
from threading import Lock
import gammu

lock = Lock()

dummy = MODEM['mode'] == 'dummy'


if not dummy:
    sm = gammu.StateMachine()
    sm.ReadConfig()
    sm.Init()

def send(sms):
    message = {
        'Text': sms['text'],
        'SMSC': MODEM['smsc'],
        'Number': sms['number'],
    }
    if not dummy:
        return sm.SendSMS(message)
    else:
        return False

def read():
    smss = []
    if not dummy:
        status = sm.GetSMSStatus()
        remain = status['SIMUsed'] + status['PhoneUsed'] + \
                 status['TemplatesUsed']
        start = True
        try:
            while remain > 0:
                if start:
                    sms = sm.GetNextSMS(Start=True, Folder=0)
                    start = False
                else:
                    sms = sm.GetNextSMS(Location=sms[0]['Location'], Folder=0)
                remain = remain - len(sms)
                for m in sms:
                    smss.append({
                        'Text': m['Text'],
                        'Number': m['Number'],
                        'DateTime': m['DateTime'],
                    })
                    sm.DeleteSMS(Folder=m['Folder'],
                                 Location=int(str(m['Location'])[-4:]))
        except gammu.ERR_EMPTY:
            pass
    lock.release()
    headers = {'content-type':'application/json'}
    return requests.post(REMOTE['sms'], data=json.dumps(smss), headers=headers)