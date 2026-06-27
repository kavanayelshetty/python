line = input("Enter a line of text: ")

words = line.split()

count = len(words)

print("Number of words:", count)


text = "Python"

print("Original:", text)
print("Reverse:", text[::-1])