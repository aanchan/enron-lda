from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import tokenize


def calculate_compound_sentiment(sentences):
    analyzer = SentimentIntensityAnalyzer()
    compound_sentiment = 0
    num_sentences = len(sentences)
    for sentence in sentences:
        vs_dict = analyzer.polarity_scores(sentence)
        compound_score = vs_dict['compound']
        compound_sentiment = compound_sentiment + compound_score

    avg_compound_sentiment = compound_sentiment / num_sentences
    return avg_compound_sentiment


def classify_sentiment(avg_compound_sentiment):
    sentiment_string = ''
    if avg_compound_sentiment >= 0.05:
        sentiment_string = 'positive'
    elif -0.05 < avg_compound_sentiment < 0.05:
        sentiment_string = 'neutral'
    elif avg_compound_sentiment <= -0.05:
        sentiment_string = 'negative'
    return sentiment_string


def get_sentiment(processed_string):
    if processed_string:
        sentences = tokenize.sent_tokenize(processed_string)
        avg_compound_sentiment = calculate_compound_sentiment(sentences)
        sentiment_string = classify_sentiment(avg_compound_sentiment)
        return sentiment_string
    else:
        raise(ValueError('An empty string was provided for sentiment Analysis'))