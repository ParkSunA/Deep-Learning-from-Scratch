import numpy as np
# 구조는 다음과 같다
"""
            (1)      (1)
 (1)  w(1)   a(1)1   w(2)   a(2)1   w(3)   y1
(x1)  w(1)   a(1)2   w(2)   a(2)1   w(3)   y2
(x2)  w(1)   a(1)3
"""
# 입력
x = np.array([1.0,0.5])
# 1층
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(x, W1) + B1

# 활성화 함수로 시그모이드 사용
def sigmoid(x):
    return 1/(1+np.exp(-x))

Z1 = sigmoid(A1)

# 2층
W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)

# 출력층 활성화 함수 정의
# 그냥 항등 함수 사용
def identity_function(X):
    return x

# 마지막 3층
W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

A3 = np.dot(Z2,W3) + B3
# 출력
Y = identity_function(A3)

print(Y)
