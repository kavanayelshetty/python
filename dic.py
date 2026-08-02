import numpy as np
var=np.array([[[1,2,3],[0,9,6],[3,9,5],[7,6,1]]])
print(var)

var2 = np.array([1,2,3])
for i in np.nditer(var2,op_flags=['readwrite']):
    i[...]=i*2
print(var2)

arr = np.array([[1,2],[2,4]])
it=np.nditer(arr,flags=['multi_index'])
for x in it:
    print(it.multi_index,x)   

vr1=np.array([[1,4,6],[3,5,8]])
vr2=np.array([[2,9,1],[4,6,7]]) 

ar=np.concatenate((vr1,vr2),axis=0)
print(ar)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

text = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)    

n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c