from nltk.sentiment.vader import SentimentIntensityAnalyzer


def analyze_sentiment(reviews):
    sid = SentimentIntensityAnalyzer()
    sentiments = [
        sid.polarity_scores(review)['compound'] for review in reviews
    ]
    return sentiments
