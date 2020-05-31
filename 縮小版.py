from scipy import optimize
import numpy as np

# パルス数
NP = 7
# 振幅１の搬送波の傾き
d = np.pi/2*(NP+1)



def f(x):
    return np.sin(x)

def g(x):
    return (-1)**i*(x/d-2*j)

def h(x):
    return f(x)-g(x)


# 変数初期化
j = 1
i = 1

for j in range(1,NP+1,1):
    for i in range(1,3,1):
        print(optimize.fsolve(h,0))
