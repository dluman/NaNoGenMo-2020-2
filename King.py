from POS import Sentence
from Vader import Sentiment

class Bio:

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.meanness = self.assess_meanness()
        self.generate_sentence()

    def assess_meanness(self):
        meanness = 1
        sentiment = Sentiment.classify(
            self.text
        )["compound"]
        if sentiment < -.5:
            meanness = "mean"
        elif sentiment < -.25:
            meanness = "kinda mean"
        elif sentiment < .25:
            meanness = "kinda nice"
        elif sentiment > .25:
            meanness = "nice"
        return meanness

    def generate_sentence(self):
        sents = Sentence.make(self.text)
        print(f"Main meanness: {self.meanness}")
        for sent in sents:
            print(Sentiment.classify(
                sent
            )["compound"]
            )
        print(sents)
