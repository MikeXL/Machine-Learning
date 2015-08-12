
# coding: utf-8

train_samples = {
    'That was the worst movie I have ever seen': 'neg',
    'I love you and you are a good person': 'pos',
    'Hadoop is the coolest program ever' : 'pos',
    'You did a nice job singing in the choir yesterday!' : 'pos',
    'not a good day.' : 'neg',
    'good are things are happening. lol' : 'pos',
    'I am so mad' : 'neg',
    'I am so rich' : 'pos',
    'I hate brownies. They are too rich' : 'neg',
    'I love brownies. They are so rich' : 'pos',
    'Rainbows make me want to cry' : 'neg',
    'I love to watch rainbows - they make me happy' : 'pos',
    'I hate coffee' : 'neg',
    'I love coffee' : 'pos',
    'You make me frown' : 'neg',
    'You make me smile' : 'pos',
}

import nltk
from nltk.classify import NaiveBayesClassifier


# In[3]:

def create_dictionary(comment):
    return dict([(word, True) for word in nltk.word_tokenize(comment)])


# In[5]:

positive_comments = []
negative_comments = []

for comments, label in train_samples.items():
    if label == 'pos' :
        positive_comments.append(comments.lower())
    else :
        negative_comments.append(comments.lower())

print positive_comments
print negative_comments


# In[7]:

# prep the python array into features
negative_features = [(create_dictionary(comment), 'neg') for comment in negative_comments]
print negative_features


# In[8]:

positive_features = [(create_dictionary(comment), 'pos') for comment in positive_comments]
print positive_features


# In[9]:

training_features = positive_features + negative_features


# In[10]:

training_features


# In[11]:

classifier = NaiveBayesClassifier.train(training_features)
classifier.show_most_informative_features()


# In[12]:

classifier.classify(create_dictionary("I love my new job"))
classifier.classify(create_dictionary("worst coffee ever, yak"))
classifier.classify(create_dictionary("life is too short for bad coffee"))
classifier.classify(create_dictionary("that was awesome"))
