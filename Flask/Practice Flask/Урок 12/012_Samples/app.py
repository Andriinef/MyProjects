import logging

from config import LOGGER_CONFIG
from flask import Flask
from flask.logging import default_handler

# from logging.handlers import FileHandler


app = Flask(__name__)

handler = logging.FileHandler("flask_app.log")
handler.setLevel(logging.DEBUG)
handler.setFormatter(LOGGER_CONFIG["formatter"])
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(LOGGER_CONFIG["formatter"])
app.logger.addHandler(ch)

app.logger.removeHandler(default_handler)

import views
