from nltk.sentiment.vader import SentimentIntensityAnalyzer as sentimentalizer

class Sentiment:

    @staticmethod
    def classify(text):
        return sentimentalizer().polarity_scores(text)
