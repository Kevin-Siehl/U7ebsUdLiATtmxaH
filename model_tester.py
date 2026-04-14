import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("ACME-HappinessSurvey2020.csv")

# Separate inputs and output
X = df.drop(columns=["Y"])
y = df["Y"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Evaluate
r2 = model.score(X, y)

print("R^2:", r2)

print(df["Y"].dtype)
print(df.isna().sum())
print(df.describe())

from sklearn.preprocessing import PolynomialFeatures
#from sklearn.linear_model import LinearRegression

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

print("R^2 with interactions:", model.score(X_poly, y))

from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
#from sklearn.preprocessing import PolynomialFeatures

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)

print("Train R^2:", model.score(X_train_poly, y_train))
print("Test R^2:", model.score(X_test_poly, y_test))

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(max_depth=3) #just decisiontree would be classification
model.fit(X_train, y_train)

print("decision tree Test R^2:", model.score(X_test, y_test))

#regression continuous vs classification (category) discreet yes/no (binary outcome)

# features ind
# target dep

#label is what trying to predict

# algorithms: logistic regression round
# 