num = 28
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")

text = "python programming"
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)

numbers = [1, 2, 3, 2, 4, 5, 1, 6]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("List without duplicates:", unique)