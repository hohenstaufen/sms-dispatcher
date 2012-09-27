ENABLE_RQ_DASHBOARD = True

MODEM = {
    'port': '/dev/ttyUSB0',
    'mode': 'dummy',
    'smsc': {'Location':1},
    'number': '+0123456789',
}

REMOTE = {
    'sms': 'http://localhost:8000/api/received/'
}

try:
    from local_settings import *
except ImportError:
    pass

