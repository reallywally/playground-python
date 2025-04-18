import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("./diabetes.csv")
train, test = train_test_split(data, test_size=0.05, shuffle=True)

train_x = train.drop(columns=["Outcome"])
train_y = train["Outcome"]
test_x = test.drop(columns=["Outcome"])
test_y = test["Outcome"]

model = XGBRegressor()
model.fit(train_x, train_y)

predict_train = model.predict(train_x)
predict_test = model.predict(test_x)

accuracy_score_train = accuracy_score(train_y, predict_train)
print(f"Accuracy_Test: {accuracy_score_train}")

accuracy_score_test = accuracy_score(test_y, predict_test)
print(f"Accuracy_Train: {accuracy_score_test}")

print(model.feature_importances_)
