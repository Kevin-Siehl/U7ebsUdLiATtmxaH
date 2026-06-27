import pandas as pd

# Modeling tools
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Evaluation
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import random
init_seed=random.randrange(1000,9999)

# -----------------------------
# Load data
# -----------------------------
data = pd.read_csv("ACME-HappinessSurvey2020.csv")

# Example:
# Replace 'target' with your actual target column
X = data.drop(columns=['Y'])
y = data['Y']

# -----------------------------
# Train/test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=init_seed,
    stratify=y
)

# -----------------------------
# Scale features
# VERY important for KNN
# -----------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# Create and train model
# -----------------------------
knn = KNeighborsClassifier(
    n_neighbors=5,
    weights='uniform',
    metric='minkowski',
    p=1
)

knn.fit(X_train_scaled, y_train)

# -----------------------------
# Predictions
# -----------------------------
y_pred = knn.predict(X_test_scaled)

# -----------------------------
# Evaluation
# -----------------------------
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))