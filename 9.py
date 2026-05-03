class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"car brand: {self.brand} , model: {self.model}")

my_car=car("toyota","corolla")
my_car.display_info()            
        
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hello! my name is  {self.name} ane i am {self.age} years old  ")
info=person("arun",19)            
print(info.greet())                