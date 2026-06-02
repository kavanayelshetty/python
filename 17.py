for i in range(1,6):
    print("⭐ "*i)

import random
import string

chars=string.ascii_letters+string.digits+"@#$%"

password="".join(random.choice(chars)for i in range(10))
print("geneted password: ",password) 

import time

for i in range(101):
    bar = "█" * (i//5) + "-" * (20 - i//5)
    print(f"\r[{bar}] {i}%", end="")
    time.sleep(0.05)

print("\nUPLOAD COMPLETE 🚀")

import random

while True:
    roll = random.randint(1, 6)
    print("🎲 You rolled:", roll)

    again = input("Roll again? (yes/no): ").lower()

    if again != "yes":
        print("Game Over!")
        break

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