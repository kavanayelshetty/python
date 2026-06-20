# Swap two numbers without using a third variable

a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

# Swap first and last element of a list

numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)


# Reverse each word in a sentence

text = "Python is fun"
for word in text.split():
    print(word[::-1], end=" ")


# Check whether a number is a perfect square
num = 49
root = int(num ** 0.5)
if root * root == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")  

# Convert decimal number to binary

num = 13
binary = bin(num)
print("Binary:", binary)      

# Print numbers from 1 to 20 that are divisible by 3

for i in range(1, 21):
    if i % 3 == 0:
        print(i)

# Check whether a year is a leap year

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")        

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)    


text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels =", count)


lst = [10, 20, 30, 40, 50]

lst[0], lst[-1] = lst[-1], lst[0]

print("Updated List:", lst)