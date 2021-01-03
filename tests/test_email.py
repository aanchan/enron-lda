import pytest
from nlp_code.email_processor import process_email, read_email_file
from nlp_code.sentiment import get_sentiment
from nlp_code.entities import get_entities
from application import create_app, register_views

@pytest.fixture()
def nsfw_email():
    data_path = 'data/maildir/lenhart-m/sent/sent/780.'
    yield read_email_file(data_path)

@pytest.fixture()
def personal_email():
    data_path = 'data/maildir/giron-d/sent/sent/186.'
    yield read_email_file(data_path)

@pytest.fixture()
def oil_and_gas_email():
    data_path='data/maildir/shankman-j/sent/sent/825.'
    yield read_email_file(data_path)

@pytest.fixture()
def oil_and_gas_email_1():
    data_path='data/maildir/fossum-d/sent/sent/118.'
    yield read_email_file(data_path)

@pytest.fixture(scope='session')
def app():
    app_context=create_app()
    register_views(app_context)
    yield app_context


@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as c:
        yield c

def test_email_parsing(oil_and_gas_email_1):
    #GIVEN : An email as a list of lines
    #WHEN process_email is called
    returned_string = process_email(oil_and_gas_email_1)
    #THEN a json structure of the email text
    sentiment = get_sentiment(processed_string=returned_string)
    #is returned
    entity_list = get_entities(email_string=returned_string)
    assert isinstance(sentiment, str)
    assert isinstance(entity_list, list)

def test_nsfw_email(client, nsfw_email):
    # GIVEN a NSFW email
    # WHEN the process-email endpoint is called
    # THEN
    #   1. the response is a success
    #   2. A sentiment is present in the JSON structure
    #   3. The topic is not present in the JSON structure
    #   4. No entities are present in the JSON structure
    rv = client.get('/process-email', json=nsfw_email)
    assert rv.status == '200 OK'
    assert 'entities' not in rv.json
    assert 'sentiment' in rv.json
    assert 'topic' not in rv.json

def test_enron_email_1(client, oil_and_gas_email_1):
    #GIVEN an exemplar Enron Oil and Gas Email
    #WHEN the process-email endpoint is called
    #THEN
    #   1. the response is a success
    #   2. A sentiment is present in the JSON structure
    #   3. The topic is classified as Enron Oil and Gas
    #   4. The ORG and PERSON entities are present
    rv = client.get('/process-email', json=oil_and_gas_email_1)
    assert rv.status == '200 OK'
    assert 'entities' in rv.json
    assert 'sentiment' in rv.json
    assert 'topic' in rv.json


def test_enron_email(client, oil_and_gas_email):
    # GIVEN an exemplar Enron Oil and Gas Email
    # WHEN the process-email endpoint is called
    # THEN
    #   1. the response is a success
    #   2. A sentiment is present in the JSON structure
    #   3. The topic is classified as Enron Oil and Gas
    #   4. The ORG and PERSON entities are present
    rv = client.get('/process-email', json=oil_and_gas_email)
    assert rv.status == '200 OK'
    assert 'entities' in rv.json
    assert 'sentiment' in rv.json
    assert 'topic' in rv.json

def test_personal_email(client, personal_email):
    # GIVEN a personal email
    # WHEN the process-email endpoint is called
    # THEN
    #   1. the response is a success
    #   2. A sentiment is present in the JSON structure
    #   3. The topic is not present in the JSON structure
    #   4. No entities are present in the JSON structure
    rv = client.get('/process-email', json=personal_email)
    assert rv.status == '200 OK'
    assert 'entities' not in rv.json
    assert 'sentiment' in rv.json
    assert 'topic' not in rv.json


