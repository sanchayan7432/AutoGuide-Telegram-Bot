from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def word_count(text):
    return len(text.split())

def semantic_similarity(a, b):
    vect = TfidfVectorizer().fit([a, b])
    tfidf = vect.transform([a, b])
    return cosine_similarity(tfidf[0], tfidf[1])[0][0]