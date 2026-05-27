#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import recall_score, classification_report, confusion_matrix, precision_score, f1_score

import random
import math

from sklearn.metrics import make_scorer, recall_score


# In[2]:


# Load data
data = pd.read_csv("ACME-HappinessSurvey2020.csv")

# Separate features and target
X = data.drop("Y", axis=1)
y = data["Y"]


# In[3]:


test_split_seed = 5678 #random.randrange(1000,9999)
#print(test_split_seed)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=test_split_seed
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[4]:


from sklearn.model_selection import GridSearchCV

dt = KNeighborsClassifier()

param_grid = {
    'n_neighbors': [1, 3, 5, 7, 9, 11],
    'weights': ['uniform', 'distance'],
    'p': [1, 2, 3]
}
scoring_criteria = make_scorer(recall_score, pos_label=1)
#scoring_criteria = make_scorer(precision_score, pos_label=1)
#scoring_criteria = make_scorer(f1_score, pos_label=1)
grid = GridSearchCV(
    dt,
    param_grid,
    scoring= scoring_criteria, #'recall',
    cv=5
)

grid.fit(X_train, y_train)


# In[5]:


# Make predictions
y_pred = grid.predict(X_test)

# Evaluate
#print("recall:", recall_score(y_test, y_pred, pos_label=0))
#recall.append(recall_score(y_test, y_pred, pos_label=0))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
#print(test_split_seed)


# In[7]:


""" for seed 1234
precision one gives:
Classification Report:
              precision    recall  f1-score   support

           0       0.86      0.43      0.57        14
           1       0.58      0.92      0.71        12

    accuracy                           0.65        26
   macro avg       0.72      0.67      0.64        26
weighted avg       0.73      0.65      0.64        26

Confusion Matrix:
[[ 6  8]
 [ 1 11]]

recall zero gives:
Classification Report:
              precision    recall  f1-score   support

           0       0.80      0.29      0.42        14
           1       0.52      0.92      0.67        12

    accuracy                           0.58        26
   macro avg       0.66      0.60      0.54        26
weighted avg       0.67      0.58      0.53        26

Confusion Matrix:
[[ 4 10]
 [ 1 11]]

precision zero and recall one gives:
Classification Report:
              precision    recall  f1-score   support

           0       0.62      0.36      0.45        14
           1       0.50      0.75      0.60        12

    accuracy                           0.54        26
   macro avg       0.56      0.55      0.53        26
weighted avg       0.57      0.54      0.52        26

Confusion Matrix:
[[5 9]
 [3 9]]

f1 one gives:
Classification Report:
              precision    recall  f1-score   support

           0       0.57      0.29      0.38        14
           1       0.47      0.75      0.58        12

    accuracy                           0.50        26
   macro avg       0.52      0.52      0.48        26
weighted avg       0.53      0.50      0.47        26


Confusion Matrix:
[[ 4 10]
 [ 3  9]]

f1 zero gives:
Classification Report:
              precision    recall  f1-score   support

           0       0.75      0.43      0.55        14
           1       0.56      0.83      0.67        12

    accuracy                           0.62        26
   macro avg       0.65      0.63      0.61        26
weighted avg       0.66      0.62      0.60        26


Confusion Matrix:
[[ 6  8]
 [ 2 10]]
 """


# In[ ]:




