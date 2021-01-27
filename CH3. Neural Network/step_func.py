def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
# step_function(x)은 실수만 입력 가능하다. 즉 배열을 인수 x로 넣을 수 없다.
# step_function(3.0) OK, step_function(np.array([1,2])) Not OK
# 넘파이 배열도 지원 가능하게 수정하면 다음과 같다.

import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    y = x > 0
    return y.astype(np.int)
# 이렇게 간단하게 구현할 수 있는 이유는 넘파이 배열을 인풋으로 받기 때문이다.
# 계단 함수 그래프
x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

# 계단 함수 출력값 확인
x = np.array([-1,1.0,2.0])
print(x)
y = x > 0
print(y)
print(y.astype(np.int))
print(step_function(x))