for i in range(1,6):
    print("⭐ "*i)

import random
import string

chars=string.ascii_letters+string.digits+"@#$%"

password="".join(random.choice(chars)for i in range(10))
print("geneted password: ",password) 

import time

# for i in range(101):
#     bar = "█" * (i//5) + "-" * (20 - i//5)
#     print(f"\r[{bar}] {i}%", end="")
#     time.sleep(0.05)

# print("\nUPLOAD COMPLETE 🚀")

import random

# while True:
#     roll = random.randint(1, 6)
#     print("🎲 You rolled:", roll)

#     again = input("Roll again? (yes/no): ").lower()

#     if again != "yes":
#         print("Game Over!")
#         break

numbers = [12, 5, 8, 20, 3]

largest = max(numbers)
smallest = min(numbers)
total = sum(numbers)

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)

text="python"
print(text[::-1])

nums=[5,9,2,14,7]
print(max(nums))

for i in range(1,6):
    print("* " * i)

    num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

for i in range(1, 6):
    print(i)  

import random

messages = [
    "Keep learning!",
    "Stay focused!",
    "You can do it!",
    "Never give up!"
]

print(random.choice(messages))      

text="python"

count=0
for ch in text:
    if ch in "aeioyAEIOU":
        count+=1
print("vowels: ",count)        

num=1234
count=len(str(num))
print("digits: ",count)

numbers=[45,12,89,23,67]
largest1=max(numbers)
print("Largest: ",largest1)

import random

chars = "abcdefghijklmnopqrstuvwxyz123456789"
password = ""

for i in range(8):
    password += random.choice(chars)

print(password)

from time import strftime

print(strftime("%H:%M:%S"))

# import qrcode
# url="https://in.pinterest.com/glowoutfitworld47/"

# img = qrcode.make(url)
# img.save("pinterest_qr.png")
# print("pinterest qrcode created")

# import qrcode
# url="https://www.linkedin.com/in/kavana-yelshetty-770954381/"

# img = qrcode.make(url)
# img.save("linkdin_qr.png")
# print("linkdin qrcode created")

try:
    a=int(input("enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("you cant divide by zero! ")    

try:
    num=int(input("enter a number: "))
    result=10/num
    print("result: ",result)
except ZeroDivisionError:
    print("cannot divide by zero!")
except ValueError:
    print("please enter a valid number.")

text = "Python is fun"

words = text.split()

for word in words:
    print(word[::-1], end=" ")        

for i in range(1, 6):
    print(str(i) * i)

expenses=[120,250,80,150]
print("total expenses=",sum(expenses))  

import random
emojis=["😊","🚀","🔥","💻"]
print(random.choice(emojis))

word = input("enter a word: ")
vowels="aeiouAEIOU"
count=0
for letter in word:
    if letter in vowels:
        count+=1
print("number of vowels: ",count)   

# Find the largest number in a list

numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

import numpy as np
arr=np.array([10,20,30,40,50])
print("original array: ",arr)
print("sliced array: ",arr[1:4])

import numpy as np
arr=np.array([10,20,30,40,50])
print("original array: ",np.max(arr))
print("sliced array: ",np.min(arr))

n = input("Enter a number: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Swap two numbers

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)    


