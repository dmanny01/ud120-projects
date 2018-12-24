#!/usr/bin/python

import pickle
import numpy as np
np.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_all = vectorizer.get_feature_names()
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
import pandas as pd
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
importances = clf.feature_importances_
#for name, imp in zip(features_all, importances):
#    print 'Name:', name , ' imp: ', imp
feature_importances = pd.DataFrame(clf.feature_importances_,
                                   index = features_all,
                                    columns=['importance'])

for no, (feature, row) in enumerate(feature_importances.iterrows()):
    if row['importance'] >= 0.2:
        print 'index: {0} feature:{1} importance:{2}'.format(no, feature, row['importance'])

print 'Accurecy: ', clf.score(features_test, labels_test)
