import string
import spacy

from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS

PARSER = English()
PUNCTUATIONS = string.punctuation + '“”’–…'
NLP = spacy.load("en_core_web_sm")

class Analyzer():
    def __init__(self, paragraphs):
        super(Analyzer, self).__init__()

        self.paragraphs = paragraphs

    def tokenize(text):
        tokens = PARSER(text)

        # Lemmatize and lowercase.
        tokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens ]

        # Remove stopwords.
        tokens = [ word for word in tokens if word not in STOP_WORDS and word not in PUNCTUATIONS ]

        return tokens

    def preprocess(self, arg):
        return Analyzer.tokenize(''.join(self.paragraphs).strip())

    # Computes the term frequency-inverse document frequency for the paragraphs.
    def tfidf_dict(self):
        tfidf_vector = TfidfVectorizer(tokenizer = self.preprocess)
        tfidf = tfidf_vector.fit_transform(self.paragraphs)
        feature_names = tfidf_vector.get_feature_names()
        corpus_index = [sent for sent in self.paragraphs]
        rows, cols = tfidf.nonzero()
        tfidf_dict = {}

        # Collects the terms (and their sentence) based on their TFIDF score.
        for row, col in zip(rows, cols):
            tfidf_dict[tfidf[row, col]] = [feature_names[col], corpus_index[row]]

        return tfidf_dict

    # Gets all POST-tagged nouns from the text.
    def getNounDict(self):
        noun_dict = {}
        for row in range(len(self.paragraphs)):
            sent = self.paragraphs[row]
            nlp_sent = NLP(sent)

            for col in range(len(nlp_sent)):
                word = nlp_sent[col]
                preprocessed_word = word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_

                if word.pos_ == 'NOUN':
                    noun_dict[preprocessed_word] = 1

        return noun_dict

    def getRelevantWords(self):
        tfidf_dict = self.tfidf_dict()
        noun_dict = self.getNounDict()

        processed_words = []
        # Sorted is unnecessary here :D.
        for key in sorted(tfidf_dict, reverse=True):
            # We are only interested in nouns.
            if tfidf_dict[key][0] in noun_dict:
                processed_words.append(tfidf_dict[key][0])

        # Get top 3 words.
        most_common = Counter(processed_words).most_common(3)

        return (most_common[0][0], most_common[1][0], most_common[2][0])
