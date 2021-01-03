import pickle
import os
import numpy as np
from nlp_code.lda.lda_data_processing import LDAFeatureProcessing
import config


def load_lda_model():
    """
    A function that loads the LDA model from a pickle file
    in the experiment folder
    Returns:
        A gensim LDA model
    """
    model_name=os.path.join(config.EXP_DIR,'lda_model.pkl')
    with open(model_name, 'rb') as f:
        return pickle.load(f)


def load_id2word():
    """
    A function that loads the id2word Dictionary model from a pickle file
    in the experiment folder
    Returns:
        A a Gensim Dictionary id2word data structure
    """
    id2word_model=os.path.join(config.EXP_DIR, 'id2word.pkl')
    with open(id2word_model, 'rb') as f:
        return pickle.load(f)


def lda_inference(lda_model, id2word_model, email_file):
    """
    A function that does LDA inference
    Args:
        lda_model: An LDA model trained with GenSim
        id2word: id2word model obtained with GenSim used to train the LDA model
        email_file: A processed string file containing the incoming email

    Returns:
        A string with a topic label
    """
    data = [email_file]
    lda_feat_processing = LDAFeatureProcessing(data)
    data_lemmatized = lda_feat_processing.process_data_lda()
    text = data_lemmatized[0] #during inference there is just a single document
    bow = id2word_model.doc2bow(text)
    # infer document-topic distribution
    topics = lda_model.get_document_topics(bow)
    # topics as list, take only the second value of each tuple
    topics = [y for x, y in topics]
    topic_index = np.argmax(topics)
    if topic_index in [0,1]:
        return 'Enron Oil&Gas'
    else:
        return None


def do_lda_inference(email_string):
    """
    A wrapper function that loads the LDA model
    and id2word and calls lda_inference
    Args:
        email_string: A string containing the incoming email

    Returns:
        The return value of lda_inference()
    """
    lda_model = load_lda_model()
    id2word = load_id2word()
    return lda_inference(lda_model, id2word, email_string)