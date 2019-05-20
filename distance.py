import numpy as np
from math import sqrt

n=np.array([[0.3, 1], [3.3, 7], [0.5, 4.5], [3.5, 1.5], [1, 2.3],
            [4, 6.3], [1.4, 1.9], [4.4, 1.9], [1.7, 8.9], [5.7, 2.9],
            [2, 4.1], [6, 7.1]])

new_x,new_y=4,5
stored=[]
k1=[]
k2=[]
k3=[]
for i in n:
    dis_x=(i[0]-new_x)**2
    dis_y=(i[1]-new_y)**2
    total=sqrt(dis_x+dis_y)
    stored=stored+[total]

print(stored)
stored1=stored
min1=min(stored)
stored1.remove(min1)
print(stored1)
min2=min(stored1)
print(min2)
stored1.remove(min2)
print(stored1)
min3=min(stored1)

k1=k1+[min1]
k2=k1+[min2]
k3=k2+[min3]

print("K1=",k1)
print("K2=",k2)
print("K3=",k3)


