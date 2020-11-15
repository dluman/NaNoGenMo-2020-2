import nltk
import re

from markovchain.text import MarkovText

class Sentence:

    @staticmethod
    def contains_verb(text):
        tokens = nltk.word_tokenize(text)
        pos = nltk.pos_tag(tokens)
        for p in pos:
            if "V" in p[1]:
                return True
        return False

    @staticmethod
    def remove_meta(text):
        sents = [sent for sent in text if sent.count("\n") < 2]
        sents = [sent.replace("\r"," ").replace("\n"," ") for sent in sents]
        sents = [re.sub(r"\^(\s)?","",sent) for sent in sents]
        sents = [re.sub(r"\[[0-9]{1,}\]","",sent) for sent in sents]
        sents = [re.sub(r"\[[a-zA-Z\.\s]{1,}\]","",sent) for sent in sents]
        sents = [sent.lstrip().rstrip() for sent in sents]
        sents = [sent for sent in sents if len(sent) > 30]
        sents = [sent for sent in sents if sent.lower().count("wikipedia") < 1]
        sents = [sent for sent in sents if not "stub" in sent]
        sents = [sent for sent in sents if not "p. " in sent]
        return sents

    @staticmethod
    def make(text):
        #markov_text = ""
        #markov = MarkovText()
        #markov.data(text)
        #for i in range(30):
            #markov_text += markov()
        sents = nltk.tokenize.sent_tokenize(text)
        sents = Sentence.remove_meta(sents)
        sents = [sent for sent in sents if Sentence.contains_verb(sent)]
        return sents
