import pandas as pd
s1= pd.Series(12,index=[1,2,3,4,5])
s2=pd.Series(12,index=[1,2,3,4])
print(s1+s2)

list_1=[[1,2,3,4,5],[6,7,8,9,10]]
var1=pd.DataFrame(list_1)
print(var1)

x=[3,4,5,6,7]
var=pd.Series(x)
print(var)