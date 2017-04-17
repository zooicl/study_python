import os
from urllib.request import urlretrieve

import numpy as np
import pandas as pd
import pydotplus
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
local_filename = os.path.basename(url)

if not os.path.exists(local_filename):
    print("Downloading Adult Census datasets from UCI")
    urlretrieve(url, local_filename)

names = ("age, workclass, fnlwgt, education, education-num, "
         "marital-status, occupation, relationship, race, sex, "
         "capital-gain, capital-loss, hours-per-week, "
         "native-country, income").split(', ')

data = pd.read_csv(local_filename, names=names)

target_names = data['income'].unique()

target = data['income']
features_data = data.drop('income', axis=1)
features_data = pd.get_dummies(features_data)

X = features_data.values.astype(np.float32)
y = (target.values == ' >50K').astype(np.int32)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

clf = DecisionTreeClassifier(max_depth=8)

clf.fit(X_test, y_test)
dot_data = tree.export_graphviz(clf, out_file=None, feature_names=features_data.columns, class_names=target_names)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("income.pdf")
