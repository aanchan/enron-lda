from flask import Flask
from views import EmailAPI, DefaultView
from flask_cors import CORS

def create_app():
    app_obj = Flask(__name__)
    CORS(app_obj)
    app_obj.config.from_object('config')
    return app_obj

def register_views(app_obj):
    email_view = EmailAPI.as_view('email_api')
    app_obj.add_url_rule('/process-email', view_func=email_view, methods=['GET'])

    default_view = DefaultView.as_view('default_api')
    app_obj.add_url_rule('/', view_func=default_view, methods=['GET'])


app =  create_app()
register_views(app)


