import spacy


def get_entities(email_string):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(email_string)
    entity_list = [(X.text, X.label_) for X in doc.ents]
    return entity_list
