import random

secret=random.randint(1,20)
while True:
    guess=int(input("guess a number between 1 and 20: "))
    if guess==secret:
        print("corrct! you won.")
        break
    elif guess < secret:
        print("too low!")
    else:
        print("too high!")   



password=input("enter password: ")

if len(password) >= 8 and any(i.isdigit() for i in password):
    print("strong password")
else:
    print("weak password")    

score =0
q1=input("capital of india? ") 
if q1.lower()=="delhi":
    score+=1
q2=input("5 x 6 = ")

# Quiz game

if q2=="30":
    score+=1

q3=input("python is a language? (yes/no): ")

if q3.lower()=="yes":
    score+=1

print("your score: ",score,"/3")    
