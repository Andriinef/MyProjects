from flask import make_response, render_template
from models import XRate


def get_all_rates():
    try:
        xrates = XRate.select()
        return render_template("xrates.html", xrates=xrates)
    except Exception as ex:
        return make_response(str(ex), 500)
