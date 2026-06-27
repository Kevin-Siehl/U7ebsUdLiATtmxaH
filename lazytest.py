from lazypredict.Supervised import LazyClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import pandas as pd

#data = load_breast_cancer()
data = pd.read_csv("ACME-HappinessSurvey2020.csv")
#X = data.data
X = data.drop(columns=["Y"])
#y = data.target
y = data["Y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=123)

clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(X_train, X_test, y_train, y_test)

print(models)

#print("predictions is ", predictions)