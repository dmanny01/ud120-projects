#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r"))
data_dict.pop("TOTAL")
#for key, value in data_dict.items():
#    print 'Name: ', key, ' salary: ', value['salary']
features = ["salary", "bonus"]
data = featureFormat(data_dict, features, remove_all_zeroes=False)


### your code below
for name, point in zip(data_dict.keys(), data):
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    matplotlib.pyplot.annotate( name  , xy=(salary, bonus) )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
