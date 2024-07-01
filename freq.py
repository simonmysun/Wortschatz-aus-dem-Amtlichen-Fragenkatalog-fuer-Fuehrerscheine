import spacy

nlp = spacy.load('de_core_news_sm')

nlp.max_length = 4000000

f = open('alltext')

lines = f.readlines()

s = ' '.join(map(lambda l : l.strip(), lines))

# doc = nlp(s[:100])
doc = nlp(s)

words = map(lambda x : (x.lemma_, x.text), doc)

freq = {}

class Word:
    def __init__(self, lemma):
        self.lemma = lemma
        self.freq = 0
        self.examples = set()
    def count(self, example):
        self.freq += 1
        self.examples |= { example }
    def __repr__(self):
        return '{}|{}|[{}]'.format(self.freq, self.lemma, ','.join(self.examples))

for (lemma, txt) in words:
    if lemma not in freq:
        freq[lemma] = Word(lemma)
    freq[lemma].count(txt)

counts = sorted(freq.items(), key=lambda word: word[1].freq)
counts = list(map(lambda t : str(t), map(lambda t : t[1], counts)))

print('\n'.join(counts))
