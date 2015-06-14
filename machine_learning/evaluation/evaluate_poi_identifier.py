#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn import cross_validation 
from sklearn.tree import DecisionTreeClassifier 
import numpy as np
from sklearn.metrics import *
features_train,features_test,labels_train,labels_test = cross_validation.train_test_split(features,labels,test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
prediction = clf.predict(features_test)
print "Number of POI's: ", np.count_nonzero(prediction)
print "People in Test Set: ", len(prediction) 
print "Accuracy: ", accuracy_score(prediction, labels_test)
print "Precision: ", precision_score(labels_test,prediction)
print "Recall: ", recall_score(labels_test,prediction)

from collections import Counter
confusion_matrix = Counter()

#truth = labels_test
prediction = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
truth = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
positives = [1]

binary_truth = [x in positives for x in truth]
binary_prediction = [x in positives for x in prediction]
for t, p in zip(binary_truth, binary_prediction):
    confusion_matrix[t,p] += 1

print confusion_matrix

print "New Precision: ", precision_score(truth,prediction)
print "New Recall: ", recall_score(truth,prediction)