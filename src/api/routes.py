from app import app
from src.api.handler import DatabaseHandler
from flask_restful import Api

api = Api(app.server)

api.add_resource(
    DatabaseHandler,            # handler
    '/api/author/<author>',     # path
)