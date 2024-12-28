import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# pip install scikit-learn   


np.random.seed(42)
X = 2 * np.random.rand(100, 1)  
y = 4 + 3 * X + np.random.randn(100, 1) 

plt.scatter(X, y, color='blue', alpha=0.5)
plt.title("Generated Data")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

model = LinearRegression()
model.fit(X, y)

# 학습된 모델의 절편과 기울기 확인
print("절편 (Intercept):", model.intercept_)
print("기울기 (Slope):", model.coef_)

X_new = np.array([[0], [2]])  # X=0과 X=2일 때 예측
y_pred = model.predict(X_new)

plt.scatter(X, y, color='blue', alpha=0.5, label='Data')
plt.plot(X_new, y_pred, color='red', label='Prediction Line')  # 예측된 직선
plt.title("Linear Regression Model")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

test_X = np.array([[1.5], [3.0]])  # X=1.5, X=3.0
test_y_pred = model.predict(test_X)

print("X=1.5일 때 예측 값:", test_y_pred[0])
print("X=3.0일 때 예측 값:", test_y_pred[1])