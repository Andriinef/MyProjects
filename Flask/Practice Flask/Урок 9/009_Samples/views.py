import controllers
from app import app


@app.route("/")
def hello():
    return "Hello everybody!"


@app.route("/xrates")
def view_rates():
    return controllers.get_all_rates()
