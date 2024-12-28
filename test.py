import numpy as np
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score, r2_score, f1_score
# 1. 데이터셋 로드
wine = load_wine()
X = wine.data
y = wine.target


# 2. 데이터셋 나누기 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# 3. 데이터 정규화

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. SVM 모델 생성

svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# 5. 모델 예측

y_pred = svm_model.predict(X_test)

# 6. 평가 결과 출력

# 정확도 평가
print("Accuracy : ", accuracy_score(y_test, y_pred)) 

# 정밀도 평가
print("Precision :", precision_score(y_test, y_pred, average='macro'))

# 재현도
print("Recall :", recall_score(y_test, y_pred, average='macro'))

# F1-Score
print("F1-Score :", f1_score(y_test, y_pred, average='macro'))

# 분류 보고서
print(classification_report(y_test, y_pred))