from functools import wraps

import controllers
from app import app
from config import IP_LIST
from flask import abort, request


def check_ip(func):
    @wraps(func)
    def checker(*args, **kwds):
        if request.remote_addr not in IP_LIST:
            return abort(403)

        return func(*args, **kwds)

    return checker


@app.route("/", methods=["GET", "POST"])
def hello():
    return "Hello everybody!"


@app.route("/xrates")
def view_rates():
    return controllers.ViewAllRates().call()


@app.route("/api/xrates/<fmt>")
def api_rates(fmt):
    return controllers.GetApiRates().call(fmt)


@app.route("/update/<int:from_currency>/<int:to_currency>")
@app.route("/update/all")
def update_xrates(from_currency=None, to_currency=None):
    return controllers.UpdateRates().call(from_currency, to_currency)


@app.route("/edit/<int:from_currency>/<int:to_currency>", methods=["GET", "POST"])
@check_ip
def edit_xrate(from_currency, to_currency):
    return controllers.EditRate().call(from_currency, to_currency)


@app.route("/logs")
@check_ip
def view_logs():
    return controllers.ViewLogs().call()
