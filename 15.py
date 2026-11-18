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