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

