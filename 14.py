

word = "banana"

for ch in set(word):
    print(ch, "appears", word.count(ch), "times")

num = 7

for i in range(1, 11):
    print(num, "x", i, "=", num * i)    

num = 18
temp = num
total = 0

while temp > 0:
    total += temp % 10
    temp //= 10

if num % total == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")

numbers = [1, 2, 3, 5, 6, 7]

n = 7
expected = n * (n + 1) // 2
actual = sum(numbers)

missing = expected - actual

print("Missing number:", missing)    

celsius = 37

fahrenheit = (celsius * 9/5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

word = "programming"
frequency = {}

for ch in word:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)

numbers = [12, 45, 23, 67, 34]

numbers.remove(max(numbers))
print("Second largest:", max(numbers))

students = {
    "Asha": 85,
    "Ravi": 92,
    "Meena": 78,
    "Kiran": 88
}


sentence = "python is easy and python is powerful"
words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:")
for word, count in frequency.items():
    print(word, ":", count)
    
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()    


message = "python is fun"
encoded = ""

for letter in message:
    encoded += chr(ord(letter) + 2)

print("Encoded message:", encoded)

decoded = ""
for letter in encoded:
    decoded += chr(ord(letter) - 2)

print("Decoded message:", decoded)

items = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Headphones": 2000
}

total = 0

print("----- Shopping Bill -----")

for item, price in items.items():
    print(item, ":", price)
    total += price

discount = total * 10 / 100
final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final amount:", final_amount)

password = "Kavana@123"

if len(password) < 6:
    print("Weak Password")
elif len(password) < 10:
    print("Medium Password")
else:
    print("Strong Password")
    
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70, 80]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common elements:", common)

sentence = "python is easy and python is powerful"

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:")
for word, count in frequency.items():
    print(word, ":", count)