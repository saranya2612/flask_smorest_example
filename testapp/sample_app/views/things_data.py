from flask import Flask, render_template
from flask.views import View,MethodView
import marshmallow as ma
from flask_smorest import Blueprint
from ..models.taskmodel import Tasktracker
things_blp = Blueprint("Things", "things", url_prefix="/things", template_folder='templates', description="Details about the test app")


class TestQueryArgsSchema(ma.Schema):
    name = ma.fields.String()


# @things_blp.route("/welcome", methods=['GET'])
# class Welcome(View):
#     def get(self, args):
#         return render_template('page.html')

@things_blp.route("/")
class Things(MethodView):
    @things_blp.arguments(TestQueryArgsSchema, location="query")
    @things_blp.response(200)
    def get(self, args):
        """List Things"""
        return [{'name': args['name']}]

    @things_blp.response(201)
    def post(self, new_data):
        """Add a new thing"""
        item = Things.addthing(**new_data)
        return item
