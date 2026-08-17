s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")