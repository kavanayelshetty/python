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

n = int(input("enter the number of terms: "))
first=0
second=1
print("fibonacci sequence: ")
for i in range(n):
    print(first,end=" ")
    next_term=first+second
    first=second
    second=next_term

my_list=[10,20,30,40]
print("list elements: ",my_list)
my_list.insert(2,25)
print("after inserting 25 at the index 2: ",my_list)
my_list.remove(20)
print("after removing 20: ",my_list)
my_list.append(50)
print("after appending 50: ",my_list)
length=len(my_list)
print("length of the list: ",length)
popped_element=my_list.pop()
print("popped element: ",popped_element)
my_list.clear()
print("after clearing the list: ",my_list)