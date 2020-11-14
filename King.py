from Vader import Sentiment

class Bio:

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.meanness = self.assess_meanness()

    def assess_meanness(self):
        meanness = 1
        sentiment = Sentiment.classify(
            self.text
        )["compound"]
        if sentiment < -.5:
            meanness = 4
        elif sentiment < -.25:
            meanness = 3
        elif sentiment < .25:
            meanness = 2
        elif sentiment > .25:
            meanness = 1
        print(sentiment) 
        return meanness

    def generate_sentence(self):
        pass
