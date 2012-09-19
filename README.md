sms-dispatcher
=========

sms-dispatcher is a sort of middleware (written in python) that offers a web API to send and receive sms from a serial modem. It is based on [Flask] and relies on [Gammu] python bindings.



Requirements
------------
Requirements are listed in `requirements/default` and `requirements/optional` files; you can install them using [pip].
You need to have a [redis] daemon on your machine; keep in mind that you will also need a working Gammu setup.
If you are using [virtualenv] with [virtualenvwrapper], you have to use the `--system-site-packages` option, in order to access to Gammu python bindings that comes with the Gammu package.

Configuration
-------------
The `settings.py` file is more or less self-explaining:

* `ENABLE_RQ_DASHBOARD` enables [RQDashboard] on `/rq`; you need to have installed optional requirements for that
* `MODEM` settings regarding your modem. If `mode` is set to "dummy", it won't do anything useful, but it will run regardless of having Gammu installed or not (only used for development). Set it to "rw" on a production environment.
* `REMOTE` defines what service will be called new sms's are received. sms-dispatcher will perform a post on that address, containing a json with the new messages.

At the moment, you need to add an entry to crontab (see `scripts/crontab.entry.example`) or call the `receive` method manually, in order to check if any new message has been received.

Startup
-------
You can use `scripts/run.sh.example` as a sample startup script. It will fire up a Flask instance and a [rqworker]. You can also do it manually, if you prefer.

[Gammu]:http://wammu.eu/gammu/
[pip]:http://pypi.python.org/pypi/pip/
[virtualenv]:http://pypi.python.org/pypi/virtualenv
[virtualenvwrapper]:https://bitbucket.org/dhellmann/virtualenvwrapper
[RQDashboard]:https://github.com/nvie/rq-dashboard
[rqworker]:http://python-rq.org/docs/workers/
[Flask]:http://flask.pocoo.org/
[redis]:http://redis.io/
