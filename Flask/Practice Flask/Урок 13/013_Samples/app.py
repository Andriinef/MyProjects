import logging
from logging.config import dictConfig

from config import LOGGING
from flask import Flask
from flask.logging import default_handler

dictConfig(LOGGING)
app = Flask(__name__)

app.logger = logging.getLogger("GoldenEye")
app.logger.removeHandler(default_handler)

import views
