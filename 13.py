import numpy as np
a=np.zeros((4))
b=np.zeros((3,4))
print(a)
print(b)

print(np.ones((4)))
print(np.ones((3,4)))

import pandas as pd
dic = {"a":[1,2,3,4],"b":[5,6,7,8],"c":[10,20,30,40]}
var=pd.DataFrame(dic)
print(var)

var2=var.to_csv("text.csv",index=False)

var1=pd.read_csv("C:\\Users\\Kavana\\OneDrive\\Desktop\\python project\\text.csv",skiprows=[1])
print(var1)

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)

text = "Hello Python"
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
