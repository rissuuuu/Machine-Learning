import numpy as np

xBlue=np.array([0.3,0.5,1,1.4,1.7,2])
yBlue=np.array([1,4.5,2.3,1.9,8.9,4.1])

print(xBlue)
print(yBlue)
res1=[]

for i in range(0,len(xBlue)):
    for j in range(0,len(yBlue)):
        if(i==j):
           res2=[xBlue[i],yBlue[j]]
           res1=res1+[res2]

print(res1)
