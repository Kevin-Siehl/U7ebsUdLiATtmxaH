
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import PassiveAggressiveClassifier

# Load data
data = pd.read_csv("ACME-HappinessSurvey2020.csv")

X = data.drop(columns=["Y"])
y = data["Y"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = PassiveAggressiveClassifier(
    C=0.05, #0.1,
    loss="squared_hinge",
    early_stopping=True,
    class_weight=None, #"balanced",
    average=True,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

