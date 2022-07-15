from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/user/<string:name>/<int:id_in>")
def user(name, id_in):
    return "Пользователь: " + name + " - " + str(id_in)


if __name__ == "__main__":
    app.run(debug=True)
