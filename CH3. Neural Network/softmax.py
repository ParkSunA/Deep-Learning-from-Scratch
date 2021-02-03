import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y= exp_a / sum_exp_a

    return y

a = np.array([0.1,0.5,1.0])
print(softmax(a))

# 소프트맥스 함수에 지수함수가 들어가 overflow가 발생할 가능성이 높다.
# 이를 방지하기 위해 다음과 같이 변경한다.

def softmax(a):
    # 입력 신호 중 가장 큰 값을 빼준다.
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.1,0.5,1.0])
print(softmax(a))
