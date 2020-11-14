import nltk

class Sentence:

    @staticmethod
    def contain_verb(text):
        tokens = nltk.word_tokenize(text)
        pos = nltk.pos_tag(tokens)
        for p in pos:
            if "V" in p[1]:
                return True
        return False

    @staticmethod
    def make(text):
        sents = nltk.tokenize.sent_tokenize(text)
        sents = [sent for sent in sents if Sentence.contain_verb(sent)]
        return sents
