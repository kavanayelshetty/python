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