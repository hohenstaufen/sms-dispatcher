from flask import Flask, request, abort
from redis import Redis
from rq import Queue, use_connection
from settings import ENABLE_RQ_DASHBOARD
from sms import send as sms_send
from sms import read as sms_read

app = Flask(__name__)

if ENABLE_RQ_DASHBOARD:
    try:
        from rq_dashboard import RQDashboard
    except ImportError:
        pass
    else:
        RQDashboard(app)

queue = Queue(connection=Redis())


@app.route('/')
def api_root():
    return ""

@app.route('/send', methods=['POST'])
def send():
    if request.headers['Content-Type'] == 'application/json':
        for sms in request.json:
            queue.enqueue(sms_send, sms)
        return ""
    else:
        return abort(415)

@app.route('/read', methods=['GET'])
def read():
    queue.enqueue(sms_read)
    return ""


if __name__ == '__main__':
    app.run()