from flask.views import MethodView
from flask import request
from nlp_code.email_processor import process_email
from nlp_code.sentiment import get_sentiment
from nlp_code.entities import get_entities
from flask import Response
from nlp_code.lda.lda_inference import do_lda_inference
import logging
from flask import jsonify

class DefaultView(MethodView):
    def get(self):
        try:
            return "Welcome to the Enron Email Parser"
        except Exception as e:
            exception = e.args[0]
            logging.error("Exception occurred in view handler: ".format(exception), exc_info=1)
            resp_dict = {'error': exception}
            return Response(resp_dict, status=400)

request_r=request
class EmailAPI(MethodView):
    def get(self):
        try:
            json_data=request.get_json()
            returned_string = process_email(json_data)
            sentiment = get_sentiment(processed_string=returned_string)
            enron_oil_and_gas = do_lda_inference(email_string=returned_string)
            if enron_oil_and_gas:
                entity_list = get_entities(email_string=returned_string)
                return_dict = {
                    'sentiment': sentiment,
                    'topic' : enron_oil_and_gas,
                    'entities': entity_list
                }
            else :
                 return_dict = {
                     'sentiment': sentiment
                 }
            return jsonify(return_dict)
        except Exception as e:
            exception = e.args[0]
            logging.error("Exception occurred in view handler: ".format(exception), exc_info=1)
            resp_dict = {'error': exception}
            return Response(resp_dict, status=400)

