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

class laptop:
    def __init__(self,brand,price):
        self.barnd=brand
        self.price=price

    def info(self):
        print(f"laptop brand: {self.barnd} , laptop price: {self.price}")

laptop1=laptop("HP",45000)
laptop2=laptop("dell",50000)

laptop1.info()
laptop2.info()

class book:
    def __init__(self,title,author="unknown"):
        self.title=title
        self.author=author
    def show_book(self):
        print(f"title:{self.title} author:{self.author}")

book1=book("python programming")
book2=book("machine learning","andrew ng")
book1.show_book()
book2.show_book()
