from database import database
from typing import List, Set, Tuple, Dict
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import string
import re
import time
from collections import Counter
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))






def bad_or_good_grams() -> None:
    good_counter: Counter[str] = Counter()
    bad_counter: Counter[str] = Counter()

    for phrase, feeling in database:
        words: List[str] = tokenize(phrase)
        for word in words:
            if word not in stop_words:
                if feeling == 'good':
                    good_counter.update([word])
                elif feeling == 'bad':
                    bad_counter.update([word])
        

    def rank_words(good_counter:  Counter[str] , bad_counter:  Counter[str] ) ->  List[Tuple[str, int]]:
        word_scores = {}
        
        all_words = set(good_counter.keys()).union(set(bad_counter.keys()))
        
        for word in all_words:
            good_count = good_counter.get(word, 0)
            bad_count = bad_counter.get(word, 0)
            score = good_count - bad_count 
            word_scores[word] = score
        
        
        ranked_words: List[Tuple[str, int]] = sorted(word_scores.items(), key=lambda x: x[1], reverse=True)
        
        return ranked_words


    ranked_words = rank_words(good_counter, bad_counter)

    for word, score in ranked_words:
        feeling = 'good' if score > 0 else 'bad' if score < 0 else 'neutral'
        print(f"('{word}', '{score}'), ")







big_str_test = str(database)



def get_words_list(database: List[Tuple[str, str]]) -> List[str]:
    words_list: List[str] = []
    for data in database:
        words: List[str] = data[0].lower().split()
        for word in words:
            # word = word.translate(str.maketrans('', '', string.punctuation))
            word = re.sub(r"[^\w\s]", "", word)
            words_list.append(word)
    return words_list


def get_words_set(database: List[Tuple[str, str]]) -> set[str]:
    words_set: Set[str] = set()
    for data in database:
        words: List[str] = data[0].lower().split()
        for word in words:
            # word = word.translate(str.maketrans('', '', string.punctuation))
            word = re.sub(r"[^\w\s]", "", word)
            words_set.add(word)
    return words_set

def text_preprocessing(text: str) -> List[str]:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)  
    token_list = [token for token in tokens]

    return token_list

def tokenize(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()

    return tokens
# -------------------------------------------


get_words_list_start_time = time.time()
a = get_words_list(database)
get_words_list_time = time.time() - get_words_list_start_time

get_words_set_start_time = time.time()
b = get_words_set(database)
get_words_set_time = time.time() - get_words_set_start_time

text_preprocessing_start_time = time.time()
c = text_preprocessing(big_str_test)
text_preprocessing_time = time.time() - text_preprocessing_start_time

# print(a,b,c)

print("text_preprocessing execution time: %s seconds" % (text_preprocessing_time))
print("get_words_list execution time: %s seconds" % (get_words_list_time))
print("get_words_set_start_time execution time: %s seconds" % (get_words_set_time))

print("---------------------")

# print(get_unigrams_list(get_words_list(database)))
# print("---------------------")
# print(get_bigrams_list(get_words_list(database)))
# print("---------------------")
# print(get_trigrams_list(get_words_list(database)))

# print(get_unigrams_tuple(get_words_list(database)))
# print("---------------------")
# print(get_bigrams_tuple(get_words_list(database)))
# print("---------------------")
# print(get_trigrams_tuple(get_words_list(database)))

bad_or_good_grams()