import logging
from flask_smorest import Api
from flask import Flask, Blueprint

import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parents[1].as_posix())
from sample_app.routes.app_config_object import blp

app = Flask(__name__)
app.register(blp)
api = Api(app)

if '__name__' == '__main__':
    app.run(host='localhost', port=8082, debug=True)
