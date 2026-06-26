# Read a string
text = input("Enter a string: ")

# Check palindrome using slicing
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

list1 = [10, 20, 30]

list2 = list1 + [40]

print("List1:", list1)
print("List2:", list2)
