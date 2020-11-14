import math
import random

import Templates
from POS import Sentence
from Vader import Sentiment

class Bio:

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.meanness = self.assess_meanness(text)
        self.entry = None
        self.generate_entry()

    def assess_meanness(self, text):
        sentiment = Sentiment.classify(
            text
        )["compound"]
        mean_index = math.ceil(sentiment * 4)/4
        return Templates.MEANNESS[mean_index]

    def generate_entry(self):
        sents = Sentence.make(self.text)
        #print(f"Main meanness: {self.meanness}")
        #for sent in sents:
        #    print(f"{self.assess_meanness(sent)} {sent}")
        #print(sents)
        sents = random.sample(sents,int(len(sents)/2))
        self.entry = f"{random.choice(Templates.INTROS)} {self.title[0]}. {random.choice(self.meanness)} {' '.join(sents)}"
