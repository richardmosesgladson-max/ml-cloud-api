
from sklearn.linear_model import LinearRegression
import joblib

X = [[5], [10], [15]]
y = [10, 20, 30]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "house_model.pkl")

print("Model trained and saved successfully!")
