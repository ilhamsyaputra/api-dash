from flask_restful import Resource
from src.service.mongodb.DatabaseServices import DatabaseServices

class DatabaseHandler(Resource):
    def get(self, author):
        query = {
            'author': author
        }

        result = DatabaseServices.find(query)

        if result is not None:
            del result['_id']

            return result
        
        return f'NO DATA FOR { author }'