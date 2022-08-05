#!/usr/bin/env python3

import logging
from flask import Flask, Blueprint
from flask_smorest import Api

import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parents[1].as_posix())
from sample_app.views.app_config_object import blp

app = Flask(__name__)
app.config['API_TITLE'] = 'My API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'
api = Api(app)
api.register_blueprint(blp)

if '__name__' == '__main__':
    app.run(host='127.0.0.1', port=8082, debug=True)
