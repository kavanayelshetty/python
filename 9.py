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
        print(f"hello! my name is  {self.name} and i am {self.age} years old  ")
info=person("arun",19)            
print(info.greet())                

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name} is barking! ")    
        
dog1=Dog("ruby","pemorian")    
dog2=Dog("bolt","beagle")
dog1.bark()    
dog2.bark()    

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"hi! I am {self.name} i am {self.age} years old")

person1=person("anand",20)
person1.introduce()        