import pytest
from email_processor import process_email
from sentiment import get_sentiment
from entities import get_entities
from application import create_app, register_views

def read_file_as_list(data_path):
    msg_string = ''
    f = open(data_path, 'r')
    msg_string=f.read()
    f.close()
    return msg_string


@pytest.fixture()
def load_static_email():
    data_path="/home/aanchan/work/global_relay/maildir/beck-s/sent/1."
    #data_path='data/305.'
    yield read_file_as_list(data_path)

@pytest.fixture(scope='session')
def app():
    app_context=create_app()
    register_views(app_context)
    yield app_context


@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as c:
        yield c

def test_email_parsing(load_static_email):
    #GIVEN : An email as a list of lines
    #WHEN process_email is called
    returned_string = process_email(load_static_email)
    #THEN a json structure of the email text
    sentiment = get_sentiment(processed_string=returned_string)
    #is returned
    entity_list = get_entities(email_string=returned_string)
    assert isinstance(sentiment, str)
    assert isinstance(entity_list, list)



def test_email_api(client, load_static_email):
    rv = client.get('/process-email', json=load_static_email)
    assert 1




