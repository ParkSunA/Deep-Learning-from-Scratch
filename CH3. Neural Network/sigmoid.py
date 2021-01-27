import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

#시그모이드 함수 그래프
x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

# 시그모이드 함수 출력값 확인
x = np.array([-1,1,2])
print(sigmoid(x))