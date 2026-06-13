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