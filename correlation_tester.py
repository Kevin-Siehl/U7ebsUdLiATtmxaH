import pandas as pd
import numpy as np

df = pd.read_csv("ACME-HappinessSurvey2020.csv")

X = df.drop(columns=["Y"])
y = df["Y"]

# Add intercept
X_mat = np.c_[np.ones(len(X)), X.values]

# Solve least squares
coeffs = np.linalg.lstsq(X_mat, y, rcond=None)[0]

# Predicted output
y_pred = X_mat @ coeffs

# Correlation between prediction and actual
corr = np.corrcoef(y, y_pred)[0, 1]

print("Correlation of combined inputs with output:", corr)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

print("R^2:", model.score(X, y))