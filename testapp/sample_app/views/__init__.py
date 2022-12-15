

from sample_app.views.tasks import blp
from sample_app.views.things_data import things_blp
from sample_app.views.people import people_blp

blueprints = (blp, things_blp, people_blp)

__all__ = ['blueprints']