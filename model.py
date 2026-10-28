
from sklearn.linear_model import LinearRegression

X = [[5], [10], [15]]
y = [10, 20, 30]

model = LinearRegression()
model.fit(X, y)


def predict_price(size: float) -> float:
    prediction = model.predict([[size]])
    return round(float(prediction[0]), 2)
