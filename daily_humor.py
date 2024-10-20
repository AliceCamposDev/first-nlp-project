import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from data_base import data_base

stemmer = PorterStemmer() 
stop_words = set(stopwords.words('english'))

def stem(data_base):
    stemmed_data = []
    for (phrase, category) in data_base:
        stemmed_phrases = [stemmer.stem(word) for word in phrase.split() if word.lower() not in stop_words]
        stemmed_data.append((stemmed_phrases, category))
    return stemmed_data

def get_words(stemmed_data):
    words = []
    for (phrase, _) in stemmed_data:
        words += phrase
    return words

def create_feature_set(stemmed_data):
    all_words = get_words (stemmed_data)
    features = []
    for (phrase, category) in stemmed_data:
        phrase_words = set(phrase)
        feature_dict = {word: (word in phrase_words) for word in all_words}
        features.append((feature_dict, category))
    return features
    
stemmed_data = stem(data_base)
features = create_feature_set (stemmed_data)
classifier = nltk.NaiveBayesClassifier.train(features)

user_day = input("Describe with a phrase how was your day?\n")

user_day_stemmed = [stemmer.stem(word) for word in user_day.split() if word.lower() not in stop_words]
new_features = {word: (word in set(user_day_stemmed)) for word in get_words(stemmed_data)}

probabilities = classifier.prob_classify(new_features)

for category in probabilities.samples():
    print(category, probabilities.prob(category))


