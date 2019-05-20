import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression

x1=np.array([0,0.6,1.1,1.5,1.8,2.5,3,3.1,3.9,4,4.9,5,5.1])
y1=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])

x2=np.array([3,3.8,4.4,5.2,5.5,6.5,6,6.1,6.9,7,7.9,8,8.1])
y2=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1])

x=np.array([[0],[0.6],[1.1],[1.5],[1.8],[2.5],[3],[3.1],[3.9],[4],[4.9],[5],[5.1],[3],[3.8],[4.4],[5.2],[5.5],[6.5],[6],[6.1],[6.9],[7],[7.9],[8],[8.1]])
y=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])

plt.plot(x1,y1,'ro',color="green")
plt.plot(x2,y2,'ro',color="red")

classifier=LogisticRegression()
classifier.fit(x,y)
p=classifier.predict_proba([[8]])
print(p)

#for i in range(1,120,1):
#    plt.plot(i/10.0-2,model(classifier,i/10.0-2),'ro')

plt.axis([-2,10,-0.5,2])
plt.show()
