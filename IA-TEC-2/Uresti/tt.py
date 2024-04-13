import nltk
from nltk.stem import SnowballStemmer
from nltk.util import ngrams
from sklearn.metrics import pairwise
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

parrafo_1 = "Esta es una prueba. De los famosos n-gramas. Se esta usando NLTK."
parrafo_2 = "Esta es otra prueba. Esto es para el ejercicio. Usando n-gramas en clase."

def pre_procesamiento(parrafo):
    tokenized_text = nltk.word_tokenize(parrafo)
    stemmer = SnowballStemmer("spanish")
    # stemming del texto y eliminacion de puntuaciones
    stemmed_text = [stemmer.stem(word) for word in tokenized_text]
    # stemmed_text = [stemmer.stem(word) for word in tokenized_text if word.isalnum()]

    return stemmed_text


parrafos = [parrafo_1, parrafo_2]
pre_procesados = [pre_procesamiento(parrafo) for parrafo in parrafos]
print(pre_procesados)

def connvertidor_ngrams(parrafo, n):
    return list(nltk.ngrams(parrafo, n))

unigramas = [connvertidor_ngrams(parrafo, 1) for parrafo in pre_procesados]
bigramas = [connvertidor_ngrams(parrafo, 2) for parrafo in pre_procesados]
trigramas = [connvertidor_ngrams(parrafo, 3) for parrafo in pre_procesados]

print("UNIGRAMAS: ", unigramas)
print("\n")
print("BIGRAMAS: ", bigramas)
print("\n")
print("TRIGRAMAS: ", trigramas)


def generador_de_matriz(gramas_1 ,gramas_2):
    # Convertir los n-gramas en vectores de frecuencia de términos
    vectorizer = CountVectorizer().fit_transform([' '.join(grama) for grama in gramas_1 + gramas_2])

    # Calcular la similitud del coseno
    cosine_sim = cosine_similarity(vectorizer)

    return cosine_sim