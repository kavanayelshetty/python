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