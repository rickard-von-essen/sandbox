from flask import Flask, request
from flask_monitor import Monitor, ObserverLog
import influxdb
from flask_monitor.influxdb import ObserverInfluxdb
import logging
from time import sleep
from random import triangular


app = Flask(__name__)
monitor = Monitor('monitor', __name__)
app.register_blueprint(monitor)
monitor.add_observer(ObserverLog())
monitor.add_observer(ObserverInfluxdb(host='127.0.0.1',
                                      port=8086,
                                      user='',
                                      password='',
                                      db='app'))


@app.route("/")
def index():
    return "Front page"


@app.route("/status/")
def status():
    sleep(triangular(0.001, 1, 0.1))
    return "Ok"


@app.route("/crash/")
def burn():
    return "Fail!", 500


if __name__ == "__main__":
    app.logger.setLevel(logging.INFO)
    for h in app.logger.handlers:
        h.setLevel(logging.INFO)
    app.run(port=8080)


