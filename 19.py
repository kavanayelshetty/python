num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

text = "Python Programming"

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

filename = "report.pdf"

extension = filename.split(".")[-1]

print("File Extension:", extension)

# Find duplicate elements in a list

numbers = [1, 2, 3, 2, 4, 5, 1, 6]

duplicates = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate Elements:", duplicates)

text = "Python"
reverse = text[::-1]

print("Reversed String:", reverse)
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)