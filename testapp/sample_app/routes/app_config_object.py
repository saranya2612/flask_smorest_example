from flask import Flask, render_template
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint
from ..models.thingmodel import Things
blp = Blueprint("thingsapp", "thingsapp", url_prefix="/things", description="Operations on test app")


class TestQueryArgsSchema(ma.Schema):
    name = ma.fields.String()


@blp.route("/")
class Welcome(MethodView):
    @blp.arguments(TestQueryArgsSchema, location="query")
    @blp.response(200)
    def get(self, args):
        render_template('index.html')

@blp.route("/things")
class Things(MethodView):
    @blp.arguments(TestQueryArgsSchema, location="query")
    @blp.response(200)
    def get(self, args):
        """List Things"""
        return [{'name': args['name']}]

    @blp.arguments(Things)
    @blp.response(201)
    def post(self, new_data):
        """Add a new thing"""
        item = Things.addthing(**new_data)
        return item
