#!/usr/bin/env python
# coding: utf-8

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.cross_validation import cross_val_score, train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()

print(type(iris))
print(iris.keys())
print(type(iris.data))
print(iris.data.shape)
print(type(iris.target))
print(iris.target.shape)
print(iris.target[:10])
print(np.unique(iris.target))
print(iris.target_names)
print(iris.data[0])

try:
    ds = datasets.fetch_california_housing()
    ds.data.shape
    ds = datasets.fetch_20newsgroups()
    len(ds.data)
    ds.data[0][:50]
    sum([len([w for w in sample.split()]) for sample in ds.data])   
except Exception as err:
    print('skipping, works only with network connection')

# Support Vector Classifier
# =========================

clf = SVC(probability=True)
clf.fit(iris.data, iris.target)
unseen = [6.0, 2.0, 3.0, 2.0]

print(clf.predict(unseen))
print(iris.target_names[clf.predict(unseen)])
print(clf.predict_proba(unseen))

# Regression
# ==========

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [1, 2.5, 3.5, 4.8, 3.9, 5.5, 7, 8]

plt.clf()
plt.scatter(X, y, c='0.25')
plt.savefig('regression_1.png')

clf = LinearRegression()
clf.fit(X, y)
print(clf.coef_)

plt.clf()
plt.plot(X, clf.predict(X), '--', color='0.10', linewidth=1)
plt.savefig('regression_2.png')

# K-Means
# =======

km = KMeans(n_clusters=3)
km.fit(iris.data)
print(km.labels_)
print(iris.target)

tr = {1: 0, 2: 1, 0: 2}
predicted_labels = np.array([tr[i] for i in km.labels_])
sum([p == t for (p, t) in zip(predicted_labels, iris.target)])

# PCA
# ===

pca = PCA(n_components=2)    
X = StandardScaler().fit_transform(iris.data)
Y = pca.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

clf = SVC()
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
print(scores.mean())
