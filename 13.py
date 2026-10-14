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

numbers = [12, 45, 23, 67, 34]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number:", largest)

num = 13
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")