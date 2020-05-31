from scipy import optimize
import numpy as np

# パルス数
t=20
# Hz
a=1

def f(x):
    return 8*1.053*(np.sin(x*t)-np.sin(3*x*t)/9+np.sin(5*x*t)/25-np.sin(7*x*t)/49)/np.pi**2

def g(x):
    return np.sin(a*x)

def h(x):
    return f(x)-g(x)

# floatのrange関数
def drange(begin, end, step):
    n = begin
    while n+step < end:
     yield n
     n += step

list_s = list()

for i in drange(0,np.pi,0.1):
    list_s.append(optimize.fsolve(h,i))

mylist = list()


# print(list_s[5][0])

for g in range(len(list_s)):
    mylist.append(list_s[g][0])
    
new_list = sorted(mylist)

q = 1

oh_my_list = list()

for w in new_list:
    if round(q, 5) != round(w, 5):
        print(w)
        oh_my_list.append(w)
        q = w

print('---------')
print(len(oh_my_list))
print('---------')
