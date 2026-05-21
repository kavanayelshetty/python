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