# Read a string
text = input("Enter a string: ")

# Check palindrome using slicing
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")