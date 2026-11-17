num = 7

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
a = [10, 20, 30, 40]
b = [30, 40, 50, 60]

common = set(a) & set(b)

print("Common elements:", common)    