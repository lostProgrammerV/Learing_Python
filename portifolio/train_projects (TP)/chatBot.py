#This  

from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')

nltk.download('punkit', quiet = True)

article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()

corpus = article.text
print(corpus)

text = corpus
sentence_list = nltk.sent_tokenize(text)

print(sentence_list)
def greeting_response(text):
    text = text.lower()
    bot_greetings = ['howdy', 'hi', 'hello', 'hey', 'hola']
    user_greetings = ['hi', 'hey', 'hello', 'hola', 'howdy']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


def bot_reponse(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_reponse = ""
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)