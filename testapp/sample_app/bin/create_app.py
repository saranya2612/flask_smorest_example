import logging
from flask_smorest import Api
from flask import Flask, Blueprint

from ..routes.app_config_object import blp


app = Flask(__name__)
app.register(blp)
api = Api(app)

if '__name__' == '__main__':
    app.run(host='localhost', port=8082, debug=True)
