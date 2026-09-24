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

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

text = "Hello World"
count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)    

numbers = [12, 45, 7, 89, 34]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

text = "Artificial Intelligence"
vowels = "aeiou"
count = 0

for ch in text.lower():
    if ch in vowels:
        count += 1

print("Number of vowels:", count)