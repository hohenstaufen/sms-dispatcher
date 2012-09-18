MODEM = {
    'port': '/dev/ttyUSB0',
    'mode': 'dummy',
    'smsc': {'Location':1},
    'number': '+0123456789',
}

REMOTE = {
    'sms': 'localhost:8000/api/sms/received/'
}

try:
    from local_settings import *
except ImportError:
    pass

