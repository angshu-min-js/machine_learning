#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time
from sklearn.metrics import accuracy_score
features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
'''
# KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=22)
t0 = time()
clf.fit(features_train, labels_train)
print "Training: ", round(time() - t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "Prediction: ", round(time() - t1, 3), "s"
print "Accuracy: ", accuracy_score(pred, labels_test)

#Training:  0.002 s
#Prediction:  0.006 s
#Accuracy:  0.944
'''

'''
# Random Forests Classifer
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=18)
t0 = time()
clf.fit(features_train, labels_train)
print "Training: ", round(time() - t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "Prediction: ", round(time() - t1, 3), "s"
print "Accuracy: ", accuracy_score(pred, labels_test)

#Training:  0.098 s
#Prediction:  0.005 s
#Accuracy:  0.92
'''

'''
# AdaBoost Classifier
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print "Training: ", round(time() - t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "Prediction: ", round(time() - t1, 3), "s"
print "Accuracy: ", accuracy_score(pred, labels_test)

#Training:  0.227 s
#Prediction:  0.016 s
#Accuracy:  0.924
'''


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
