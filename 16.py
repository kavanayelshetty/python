# #rock paper scissors

# a=input("choose rock/paper/scissor: ")
# b=input("choose rock/paper/scissor: ")

# if a==b:
#     print("draw")
# elif(a=="rock" and b=="scissors") or (a=="paper" and b=="rock") or (a=="scissor" and b=="paper"):
#     print("player 1 wins")
# else:
#     print("player 2 wins")  /


arr =[5,2,8,1,9]

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print("sorted: ",arr)     

stack=[]

stack.append(10)
stack.append(20)
stack.append(30)

print("popped: ",stack.pop())
print("stack: ",stack)


nums = [12, 45, 7, 89, 34, 89, 23]

largest = second = float('-inf')

for i in nums:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest:", second)

nums = [12, 45, 7, 89, 34, 89, 23]

largest = second = float('-inf')

for i in nums:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest:", second)

text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

secret = 7
guess=int(input("guess a number (1-10): "))

if guess==secret:
    print("correct")
else:
    print("wrong guess")    

    
# word = input("Enter a word: ")
# count = 0

# for i in word.lower():
#     if i in "aeiou":
#         count += 1

# print("Vowels:", count)

# quiz game

score=0
ans=input("python is a programming language (yes/no): ")

if ans.lower()=="yes":
    print("correct!")
    score+=1
else:
    print("wrong!") 
print("score: ",score)       

import random

while True:
    print("Dice: ",random.randint(1,6))

    again=input("Roll again? (y/n): ")
    if again=="n":
        break

import time
seconds=int(input("enter time in seconds: "))
while seconds>0:
    print("Time left: ", seconds,"seconds")
    time.sleep(1)
    seconds-=1
print("Time's up")        
