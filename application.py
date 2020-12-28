from flask import Flask
from views import EmailAPI


def create_app():
    app_obj = Flask(__name__)
    return app_obj

def register_views(app_obj):
    email_view = EmailAPI.as_view('email_api')
    app_obj.add_url_rule('/process-email', view_func=email_view, methods=['GET'])



app =  create_app()
register_views(app)


