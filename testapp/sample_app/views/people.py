from flask.views import MethodView
from flask_smorest import Blueprint, abort
import marshmallow as ma

people_blp = Blueprint('People', 'people',
              url_prefix='/people', description='Operations on people')

class QueryByNameSchema(ma.Schema):
    name = ma.fields.String()

class PersonSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()

class PersonNestedSchema(PersonSchema):
    class Meta:
        fields = ('id', 'name')

@people_blp.route('/')
class People(MethodView):

    @people_blp.arguments(QueryByNameSchema, location='query')
    @people_blp.response(200, PersonSchema(many=True))
    def get(self, args):
        """List people"""
        return []

    @people_blp.arguments(PersonSchema)
    @people_blp.response(201, PersonSchema)
    def post(self, new_data):
        """Add a new person"""
        return {}


@people_blp.route('/<person_id>')
class PeopleById(MethodView):

    @people_blp.response(200, PersonSchema)
    def get(self, person_id):
        """Get person by ID"""
        return {}

    @people_blp.arguments(PersonSchema)
    @people_blp.response(200, PersonSchema)
    def put(self, update_data, person_id):
        """Update existing person"""
        return {}

    @people_blp.response(204)
    def delete(self, person_id):
        """Delete person"""
        abort(404, message='Item not found.')