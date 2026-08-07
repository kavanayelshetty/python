numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

text = "Artificial Intelligence"

count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)