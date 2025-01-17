from data_base import data_base
from typing import List, Set, Tuple
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import string
import re
import time
                
big_str_test = str(data_base)

def get_unigrams(words: List[str]) -> List[Tuple[str]]:
    unigrams: List[Tuple[str]] = list(ngrams(words, 1))
    return unigrams
                
def get_words_list(data_base: List[Tuple[str, str]]) -> List[str]:
    words_list: List[str] = []
    for data in data_base:
        words: List[str] = data[0].lower().split()
        for word in words:
            # word = word.translate(str.maketrans('', '', string.punctuation))
            word = re.sub(r'[^\w\s]', '', word)
            words_list.append(word)
    return (words_list)
        
def get_words_set(data_base: List[Tuple[str, str]]) -> set[str]:
    words_set: Set[str] = set()
    for data in data_base:
        words: List[str] = data[0].lower().split()
        for word in words:
            # word = word.translate(str.maketrans('', '', string.punctuation))
            word = re.sub(r'[^\w\s]', '', word)
            words_set.add(word)
    return (words_set)

def text_preprocessing(text: str) -> List[str]:
    text = text.lower()
    #text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    token_list = [token for token in tokens]

    return token_list

#-------------------------------------------


get_words_list_start_time = time.time()
a = get_words_list(data_base)
get_words_list_time = time.time() - get_words_list_start_time

get_words_set_start_time = time.time()
b = get_words_set(data_base)
get_words_set_time = time.time() - get_words_set_start_time

text_preprocessing_start_time = time.time()
c = text_preprocessing(big_str_test)
text_preprocessing_time = time.time() - text_preprocessing_start_time

#print(a,b,c)

print("text_preprocessing execution time: %s seconds" % (text_preprocessing_time))
print("get_words_list execution time: %s seconds" % (get_words_list_time))
print("get_words_set_start_time execution time: %s seconds" % (get_words_set_time))

print(get_unigrams(get_words_list(data_base)))