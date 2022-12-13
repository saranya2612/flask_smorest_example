from flask import Flask, render_template
from flask.views import View,MethodView
import marshmallow as ma
from flask_smorest import Blueprint
from ..models.thingmodel import Things
blp_data = Blueprint("thingsdata", "thingsdata", url_prefix="/thingsdata", template_folder='templates', description="Details about the test app")


class TestQueryArgsSchema(ma.Schema):
    name = ma.fields.String()


# @blp_data.route("/", methods=['GET'])
# class Welcome(View):
#     def get(self, args):
#         return render_template('page.html')

@blp_data.route("/thingsdata")
class Things(MethodView):
    @blp_data.arguments(TestQueryArgsSchema, location="query")
    @blp_data.response(200)
    def get(self, args):
        """List Things"""
        return [{'name': args['name']}]

    @blp_data.arguments(Things)
    @blp_data.response(201)
    def post(self, new_data):
        """Add a new thing"""
        item = Things.addthing(**new_data)
        return item
