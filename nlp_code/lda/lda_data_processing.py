"""
This module implements data processing that is useful prior to
LDA. This module borrows some code from this blog post :
https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/
"""
import logging
import gensim
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess
import spacy


def sent_to_words(sentences):
    """
    This function converts sentences into preprocessed
    word tokens. Word tokens are preprocessed using
    gensim's simple pre-process. This does things like convert
    strings to lower-case, remove punctuations, normalize text
    containing any accent characters and remove quotes.
    Args:
        sentences: a list of sentence strings

    Returns:
        Yields a preprocessed sentence.
    """
    for sentence in sentences:
        yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations


def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """
    This function uses Spacy's lemmatizer to find base forms
    for each of the word tokens.
    Args:
        texts: An input list of word tokens from a sentence, each sentence/document
               is also a list element
        allowed_postags: allowed part of speech tags for lemmatization

    Returns:
        A list of lemmatized word tokens that belong to a list of sentences/documents
    """
    nlp = spacy.load('en', disable=['parser', 'ner'])
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out


class LDAFeatureProcessing:

    def __init__(self, data):
        logging.info("Initializing LDA feature processing")
        self.data_words = list(sent_to_words(data))
        self.stop_words=stopwords.words('english')
        self.stop_words.extend(['from', 'subject', 're', 'edu', 'use','would','thank','know',
                                'go','may','let', 'need', 'call','time','make','get','deal',
                                'say','work','see','send','think','agreement','also','attach','want','www','com'])

    def remove_stopwords(self, texts):
        """
        A function to remove stop-words
        Args:
            texts: A list of lists i.e. words in a document.

        Returns:
            A list of lists i.e. words in a document with stop words removed
        """
        return [[word for word in simple_preprocess(str(doc)) if word not in self.stop_words] for doc in texts]

    def process_data_lda(self):
        """
        Top-level function to call the various pre-processing steps.
        Note: This class contained code to create bigrams and trigrams,
        but it was eventually removed to reduce computational time,
        and to allow for rapid experimentation of multiple models.
        Returns:
            A list of lists containing lemmatized word tokens in a document
        """
        logging.info("Creating LDA features")
        data_lemmatized = lemmatization(self.data_words, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
        data_words_nostops = self.remove_stopwords(data_lemmatized)
        return data_words_nostops




