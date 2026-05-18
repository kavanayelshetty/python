import random
secret=random.randint(1,10)
print("guess a number between 1 and 10")
guess=int(input("enter your guess: "))

if guess==secret:
    print("correct! you guessed it.")
else:
    print("wrong")
    print("the correct number was: ",secret)    