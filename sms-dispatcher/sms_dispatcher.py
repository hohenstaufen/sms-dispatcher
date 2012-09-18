from flask import Flask, request, abort
from rq import Queue, use_connection
from sms import send as sms_send
from sms import read as sms_read
from sms import lock

app = Flask(__name__)
use_connection()
queue = Queue()


@app.route('/')
def api_root():
    return

@app.route('/send', methods=['POST'])
def send():
    if request.headers['Content-Type'] == 'application/json':
        for sms in request.json:
            queue.enqueue(sms_send, sms)
        return
    else:
        return abort(415)

@app.route('/read', methods=['GET'])
def read():
    if lock.acquire(False):
        queue.enqueue(sms_read)
        return
    else:
        return abort(406)


if __name__ == '__main__':
    app.run()