from flask.views import MethodView
from flask import request
from email_processor import process_email
from sentiment import get_sentiment
from entities import get_entities
from flask import jsonify


class EmailAPI(MethodView):
    def get(self):
        json_data=request.get_json()
        #email_string=json_data['email']
        returned_string = process_email(json_data)
        sentiment = get_sentiment(processed_string=returned_string)
        entity_list = get_entities(email_string=returned_string)
        return_dict = {
            'sentiment': sentiment,
            'entities': entity_list
        }
        return jsonify(return_dict)

