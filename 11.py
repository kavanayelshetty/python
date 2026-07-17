class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"car brand: {self.brand} , model: {self.model}")

my_car=car("toyota","corolla")
my_car.display_info()   

# Python program to find the largest element in a list

numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)