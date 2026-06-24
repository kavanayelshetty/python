# import random

# secret = random.randint(1, 100)

# while True:
#     guess = int(input("Guess a number between 1 and 100: "))

#     if guess < secret:
#         print("Too low!")
#     elif guess > secret:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed it.")
#         break

import random

quotes = [
    "Success comes from consistency.",
    "Small progress is still progress.",
    "Discipline beats motivation.",
    "Keep learning every day.",
    "Focus on the process."
]

print("Quote of the Day:")
print(random.choice(quotes))

import time

print("Countdown Started!\n")

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("\nTime's Up!")