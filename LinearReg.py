from matplotlib import pyplot as plt
from sklearn import linear_model
import pandas


def prediction(m,c,x):
    y=m*x+c
    return y

x=[112,345,198,305,372,550,302,420,578]
y=[1120,1523,2102,2230,2600,3200,3409,3689,4460]
df=pandas.DataFrame({'area':x,'price':y})
print(df)
print(df.shape)
print(df.describe())
plt.scatter(df.area,df.price,color="red",marker=".")
plt.ylabel('Price of House')
plt.xlabel('Size of House')
plt.axis([0,600,0,7000])

reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
m=reg.coef_
c=reg.intercept_
plt.plot(x,m*x+c)
x=prediction(m,c,410)
print(x)
plt.show()



