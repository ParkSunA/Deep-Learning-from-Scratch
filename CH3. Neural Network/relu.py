import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0,x)

# relu 함수 그래프
x = np.arange(-5.0,5.0,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

# relu 출력값 확인
x = np.array([-1,1,2])
print(relu(x))