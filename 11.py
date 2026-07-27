def welcome(func):
    def wrapper():
        print("namaskara")
        func()
        print("take care!")
    return wrapper    
@welcome
def intro():
    print("i am kavana")
intro()

numbers = [12, 45, 7, 89, 34, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)