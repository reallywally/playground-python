import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

data = pd.read_csv("./boston.csv")

train, test = train_test_split(data, test_size=0.05, shuffle=True)

train_x = train.drop(columns=["MEDV"])
train_y = train["MEDV"]
test_x = test.drop(columns=["MEDV"])
test_y = test["MEDV"]

model = LinearRegression()
model.fit(train_x, train_y)

predict_train = model.predict(train_x)
predict_test = model.predict(test_x)

rmse_test = root_mean_squared_error(test_y, predict_test)
print(f"RMSE_Test: {rmse_test}")

rmse_train = root_mean_squared_error(train_y, predict_train)
print(f"Train RMSE: {rmse_train}")

print(model.coef_)
print(model.intercept_)