num = 14

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Multiplication Table of 7

num = 7

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

text = "Python"

reverse = text[::-1]

print("Original String:", text)
print("Reversed String:", reverse)

# Find the largest number in a list

numbers = [12, 45, 7, 89, 34, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

# Count vowels in a string

text = "Hello Python"

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)
