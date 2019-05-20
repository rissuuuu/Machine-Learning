from matplotlib import pyplot as plt
import pandas
from sklearn import linear_model


X=[100,500,200,400,300,800,700,600]
Y=[1100,2434,3356,4231,5565,6123,7654,8234]
df=pandas.DataFrame({'Size':X,'Price':Y})
plt.scatter(X,Y,color="black",marker="*")
plt.xlabel("Size of house")
plt.ylabel("Price of house")
plt.axis([0,900,0,9000])
reg=linear_model.LinearRegression()
reg.fit(df[['Size']],df.Price)
c=reg.intercept_
m=reg.coef_
print("slope",m)
print("intercept",c)

def prediction(x):
    y=m*x+c
    return y

pr=prediction(129)
print(pr)
print(df.describe())
plt.plot(X,m*X+c)
plt.show()