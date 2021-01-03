"""
This script uses an open source library called Gensim to train an LDA
model. The model is output to the folder specified in config.EXP_DIR
This module borrows some code from this blog post :
https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/
"""
#standard imports
import os
import logging
import pickle
#third-party imports

import pyLDAvis.gensim
import gensim.corpora as corpora
import gensim
from gensim.models import CoherenceModel
#local imports
from nlp_code.email_processor import read_email_file
from nlp_code.lda.lda_data_processing import LDAFeatureProcessing
import config

logging.getLogger().setLevel(logging.INFO)

def save_pickle(pkl_file, data_structure):
    """
    A function to save a data structure as a
    pickle file
    Args:
        pkl_file: str containing the pickle file name
        data_structure: the data sctructure to be pickled

    Returns:
    """
    with open(pkl_file, 'wb') as f:
        pickle.dump(data_structure, f)

def load_pickle(pkl_file):
    """
    A function to load a data structure from a
    pickle file
    Args:
        pkl_file: str containing the pickle file name
        data_structure: the data sctructure to be pickled

    Returns:
    """
    with open(pkl_file, 'rb') as f:
        data_structure = pickle.load(f)
    return data_structure


def load_data_set_into_memory():
    """
    A function to load the list of processed files
    and read their content into a string
    Returns:
        A list of email strings
    """
    cleaned_data_email_list = []
    file_name = config.PROCESSED_FILE_LIST_PATH
    with open(file_name, 'r') as f:
        for data_file_path in f.readlines():
            data_file_path = data_file_path.strip()
            logging.info("Reading email file:" + data_file_path)
            email_str = read_email_file(data_file_path)
            cleaned_data_email_list.append(email_str)
    return cleaned_data_email_list


def train_lda(exp_dir):
    """

    Args:
        exp_dir:

    Returns:

    """
    data = load_data_set_into_memory()
    logging.info("Cleaned data set loaded into memory")
    lda_feats = LDAFeatureProcessing(data)
    data_lemmatized = lda_feats.process_data_lda()
    logging.info("Created lemmatized data")
    id2word = corpora.Dictionary(data_lemmatized)
    logging.info("Created id2word data")
    # Create Corpus
    texts = data_lemmatized
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]
    logging.info("Training LDA models")
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=config.NUM_LDA_TOPICS,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=100,
                                                passes=10,
                                                alpha='auto',
                                                per_word_topics=True)

    # Compute Coherence Score
    coherence_model_lda = CoherenceModel(model=lda_model, texts=data_lemmatized, dictionary=id2word, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()

    #Write scores to the log file
    os.makedirs(exp_dir, exist_ok=True)
    with open(os.path.join(exp_dir, 'model.log'), "a") as myfile:
        myfile.write('\nCoherence Score: ' + str(coherence_lda))
        myfile.write('\nPerplexity: ' + str(lda_model.log_perplexity(corpus))+ "\n")
        for line in lda_model.print_topics():
            myfile.write(str(line) + '\n')

    file_names_dict={
        'data_lemmatized.pkl' :  data_lemmatized ,
        'lda_model.pkl' : lda_model,
        'id2word.pkl' : id2word}

    for file_name in file_names_dict.keys():
        file_name_to_write=os.path.join(exp_dir, file_name)
        save_pickle(file_name_to_write, file_names_dict[file_name])

    generate_vis(data_lemmatized, lda_model, id2word, exp_dir)

def generate_vis(data_lemmatized, lda_model, id2word, file_path):
    texts = data_lemmatized
    corpus = [id2word.doc2bow(text) for text in texts]

    #calculate the frequency of each term for analysis
    freq_dict = {key: 0 for key in id2word.token2id.keys()}
    for cp in corpus:
        for id, freq in cp:
            freq_dict[id2word[id]] = freq_dict[id2word[id]] + freq

    #Sort the dictionary of words and the associated frequency of values by value
    #And save the file to disk
    freq_dict_sorted=dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
    save_pickle(os.path.join(file_path,'freq_corpus.pkl'),freq_dict_sorted)

    vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(vis, os.path.join(file_path, 'LDA_Visualization.html'))

if __name__=="__main__":
    train_lda(config.EXP_DIR)
