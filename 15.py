num = 7

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
a = [10, 20, 30, 40]
b = [30, 40, 50, 60]

common = set(a) & set(b)

print("Common elements:", common)    

num = 153
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
num = 25
binary = bin(num)

print("Binary:", binary[2:])    

text = "programming"
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)

prices = [120, 250, 80, 150]

total = sum(prices)
discount = total * 0.10
final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final bill:", final_amount)

sentence = "python is easy and python is powerful"

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

numbers = [1, 2, 3, 5, 6, 7]

n = 7
expected = n * (n + 1) // 2
actual = sum(numbers)

missing = expected - actual

print("Missing number:", missing)

students = [
    {"name": "Asha", "age": 20},
    {"name": "Rahul", "age": 21},
    {"name": "Asha", "age": 20},
    {"name": "Priya", "age": 19}
]

unique_students = []

for student in students:
    if student not in unique_students:
        unique_students.append(student)

print(unique_students)
