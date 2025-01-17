import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from data_base import data_base

from typing import List, Tuple, Dict, Set

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))


def stem(data_base: List[Tuple[str, str]]) -> List[Tuple[list[str], str]]:
    stemmed_data: List[Tuple[list[str], str]] = []
    for phrase, category in data_base:
        stemmed_phrases: List[str] = [
            stemmer.stem(word)
            for word in phrase.split()
            if word.lower() not in stop_words
        ]
        stemmed_data.append((stemmed_phrases, category))
    return stemmed_data


def get_words(stemmed_data: List[Tuple[list[str], str]]) -> List[str]:
    words: List[str] = []
    for phrase, _ in stemmed_data:
        words += phrase
    return words


def create_feature_set(
    stemmed_data: List[Tuple[list[str], str]],
) -> List[Tuple[Dict[str, bool], str]]:
    all_words = get_words(stemmed_data)
    features: List[Tuple[Dict[str, bool], str]] = []
    for phrase, category in stemmed_data:
        phrase_words: Set[str] = set(phrase)
        feature_dict: Dict[str, bool] = {
            word: (word in phrase_words) for word in all_words
        }
        features.append((feature_dict, category))
    return features


stemmed_data: List[Tuple[list[str], str]] = stem(data_base)
features: List[Tuple[Dict[str, bool], str]] = create_feature_set(stemmed_data)
classifier = nltk.NaiveBayesClassifier.train(features)

user_day = input("Describe with a phrase how was your day?\n")

user_day_stemmed = [
    stemmer.stem(word) for word in user_day.split() if word.lower() not in stop_words
]
new_features = {
    word: (word in set(user_day_stemmed)) for word in get_words(stemmed_data)
}

probabilities = classifier.prob_classify(new_features)

for category in probabilities.samples():
    print(category, probabilities.prob(category))
