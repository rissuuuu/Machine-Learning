import numpy as np
from matplotlib import  pyplot as pl
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from math import sqrt

xBlue=[0.3,0.5,1,1.4]
yBlue=[1,4.5,2.3,1.9]

xRed=[3.3,3.5,4,4.4]
yRed=[7,1.5,6.3,1.9]

xGreen=[1.7,2,5.7,6]
yGreen=[8.9,4.1,2.9,7.1]

Xx=[]
Y=np.array([0,0,0,0,1,1,1,1,2,2,2,2])

for i in range(0,len(xBlue)):
    for j in range(0,len(yBlue)):
        if(i==j):
            res2=[xBlue[i],yBlue[i]]
            res3=[xRed[i],yRed[j]]
            res4=[xGreen[i],yGreen[i]]
            Xx=Xx+[res2]
            Xx=Xx+[res3]
            Xx=Xx+[res4]


print(Xx)
X=np.array(Xx)

pl.plot(xBlue,yBlue,'ro',color="Blue")
pl.plot(xRed,yRed,'ro',color="Red")
pl.plot(xGreen,yGreen,'ro',color="Green")
pl.axis([-0.5,10,-0.5,10])
pl.xlabel("Blue=0, Red=1")




classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,Y)
new_x,new_y=8,5
p=classifier.predict([[new_x,new_y]])
if p==0:
    pl.plot(new_x,new_y,'ro',color="Blue",markersize=15)
    print(new_x,new_y,"is Blue",p)
    pl.ylabel([new_x,new_y,"is blue"])

elif p==1:
    pl.plot(new_x,new_y,'ro',color="Red",markersize=15)
    print(new_x,new_y,"is Red",p)
    pl.ylabel([new_x,new_y,"is red"])
else:
    pl.plot(new_x, new_y, 'ro', color="Green", markersize=15)
    print(new_x, new_y, "is Green", p)
    pl.ylabel([new_x, new_y, "is Green"])


stored=[]
k1=[]
k2=[]
k3=[]
for i in X:
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
stored1.remove(min2)
print(stored1)
min3=min(stored1)

k1=k1+[min1]
k2=k1+[min2]
k3=k2+[min3]

print("K1=",k1)
print("K2=",k2)
print("K3=",k3)


pl.show()