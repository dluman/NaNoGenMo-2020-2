import math
import random

import Templates
from POS import Sentence
from Vader import Sentiment

from markovchain.text import MarkovText

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
        print(sentiment, mean_index)
        return Templates.MEANNESS[mean_index]

    def generate_entry(self):
        #markov_sents = ""
        sents = Sentence.make(self.text)
        sents = random.sample(sents,int(len(sents)/2))
        #markov = MarkovText()
        #markov.data(' '.join(sents))
        #for i in range(30):
        #    markov_sents += markov()
        #sents = random.sample(markov_sents,10)
        self.entry = f"{random.choice(Templates.INTROS)} {self.title[0]}. {random.choice(self.meanness)}\n\n{' '.join(sents)}"
