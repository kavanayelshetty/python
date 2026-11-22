

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

topper = max(students, key=students.get)

print("Student marks:", students)
print("Topper:", topper)
print("Highest marks:", students[topper])