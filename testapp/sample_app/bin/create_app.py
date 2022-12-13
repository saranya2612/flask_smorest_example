import logging
from flask import Flask, Blueprint, render_template
from flask_smorest import Api
from sample_app.views import blueprints


def root():
    return render_template('index.html')


def create_app():
    app = Flask(__name__)
    app.config['API_TITLE'] = 'My API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_JSON_PATH'] = 'api-spec.json'
    app.config['OPENAPI_URL_PREFIX'] = '/api'
    app.config['OPENAPI_REDOC_PATH'] = "/redoc"
    app.config['OPENAPI_REDOC_URL'] = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    app.config['OPENAPI_SWAGGER_UI_PATH'] = "/v1/"
    app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)
    for blp in blueprints:
        api.register_blueprint(blp)
    app.add_url_rule('/', view_func=root)

    return app
