import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import random

# Load data
data = pd.read_csv("ACME-HappinessSurvey2020.csv")

init_seed = random.randrange(1000,9999)
other_seed = random.randrange(1000,9999)

# Separate features and target
X = data.drop("Y", axis=1)
y = data["Y"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=other_seed
)

#criterion

# Create model
model = DecisionTreeClassifier(
    max_depth=None, #3,10,5  #default=none
    random_state=42,
    #random_state=init_seed,
    min_samples_split=2, #10 #default=2
    max_leaf_nodes=None,
    min_samples_leaf=5, #5  #default=1
    class_weight=None, #"balanced"
    criterion = "log_loss" # "entropy", "log_loss", default="gini"
)

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print(init_seed)
print(other_seed)