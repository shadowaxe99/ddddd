```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def tokenize(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        return [word for word in tokens if word not in self.stop_words]

    def get_sentence_similarity(self, sentence1, sentence2):
        vectorizer = TfidfVectorizer().fit_transform([sentence1, sentence2])
        vectors = vectorizer.toarray()
        return cosine_similarity(vectors)[0][1]

    def train_word2vec(self, sentences):
        model = Word2Vec(sentences, min_count=1)
        return model

def getNlp():
    nlpData = NLPProcessor()
    return nlpData
```