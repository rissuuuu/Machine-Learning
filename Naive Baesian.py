import numpy as np
from matplotlib import  pyplot as pl
from sklearn.naive_bayes import GaussianNB


X=np.array([[0.3, 1], [3.3, 7], [0.5, 4.5], [3.5, 1.5], [1, 2.3],
            [4, 6.3], [1.4, 1.9], [4.4, 1.9], [1.7, 8.9], [5.7, 2.9],
            [2, 4.1], [6, 7.1]])
Y=np.array(["Blue","Blue","Blue","Blue","Red","Red","Red","Red","Green","Green","Green","Green"])
xBlue=[0.3,0.5,1,1.4]
yBlue=[1,4.5,2.3,1.9]

xRed=[3.3,3.5,4,4.4]
yRed=[7,1.5,6.3,1.9]

xGreen=[1.7,2,5.7,6]
yGreen=[8.9,4.1,2.9,7.1]

pl.plot(xBlue,yBlue,'ro',color="Blue")
pl.plot(xRed,yRed,'ro',color="Red")
pl.plot(xGreen,yGreen,'ro',color="Green")

classifier=GaussianNB()
classifier.fit(X,Y)
p=classifier.predict([[8,5]])
pl.plot(6,8,"ro",markersize=10,color="Blue")
print(p)
pl.show()