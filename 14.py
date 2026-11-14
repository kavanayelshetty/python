import pandas as pd
s1= pd.Series(12,index=[1,2,3,4,5])
s2=pd.Series(12,index=[1,2,3,4])
print(s1+s2)

list_1=[[1,2,3,4,5],[6,7,8,9,10]]
var1=pd.DataFrame(list_1)
print(var1)

word = "banana"

for ch in set(word):
    print(ch, "appears", word.count(ch), "times")

num = 7

for i in range(1, 11):
    print(num, "x", i, "=", num * i)    