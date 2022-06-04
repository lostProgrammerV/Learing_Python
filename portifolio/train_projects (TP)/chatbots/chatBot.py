from genericpath import exists
from urllib import response
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

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp =list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index

def bot_reponse(user_input):
    user_input = 'hello world'
    sentence_list.append(user_input)
    bot_reponse = ""
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    simnilarity_scores_list = similarity_scores.flatten()
    index = index_sort(simnilarity_scores_list)
    response_flag = 0

    j = 0
    for i in range(len(index[1:])) > 0.0:
        if simnilarity_scores_list[index[i]] > 0.0:
            bot_reponse = bot_reponse + '' + sentence_list[index[i]]
            response_flag = 1
            j += 1
        if j > 2:
            break
        if response_flag == 0:
            bot_reponse = bot_reponse + ' ' + 'I apologize, I dont understand.'
        sentence_list.remove(user_input)

        return bot_reponse

print('Doc bot: I am Doctor bot. I wil answer your queries about Choronic Kidney Disease. If you want exit, type bye')

exit_list = ['exit', '']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Doc bot: Chat with you later!')
        break
    else:
        if greeting_response(user_input) != None:
            print('Doc bot:' + greeting_response(user_input))
        else:
            print('Doc bot: ' + bot_reponse(user_input))