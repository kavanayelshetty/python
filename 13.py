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

score = 0

answer = input("What is the capital of India? ")

if answer.lower() == "new delhi":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")


answer = input("What is 5 * 6? ")

if answer == "30":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")

print("Your score:", score, "/ 2")

num = 121
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")
