import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from math import exp as es

X=np.array([[10000,80000,35],[7000,120000,57],[100,23000,22],[223,18000,26]])
y=np.array([1,1,0,0])

classifier=LogisticRegression()
classifier.fit(X,y)

predict=classifier.predict([[5500,50000,25]])
print(predict)

plt.plot(X,y,'ro',color="red")



plt.axis([-30000,150000,-0.5,2])
plt.show()