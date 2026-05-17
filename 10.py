class user:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
    def get_username(self):
        return self.username
    def check_password(self,password):
        return password==self.__password

user=user("dev_kannada","pass1234")
print(user.get_username())
print(user.check_password("wrong_pass"))
print(user.check_password("pass1234"))

class car:
    def start_engine(self):
        print("engine started")
    def accelarate(self):
        print("car accelerating")
    def brake(self):
        print("car")
car = car()
car.start_engine()
car.accelarate()
car.brake()      

data="apple,banana,mango"
fruits=data.split(",")
print(fruits)

def add_numbers(a,b):
    return a+b
result = add_numbers(10,20)
print("the sum is: ",result)

class database:
    def __init__(self):
        self.__storage={}
    def save_data(self,key,value):    
        self.__storage[key]=value
        print(f"data saved for {key}")
    def get_data(self,key):
        return self.__storage.get(key,"no data found")  
db=database()
db.save_data("user_101",{"name":"raj","age":30})
print(db.get_data("user_101"))  

class family:
    def __init__(self,surname):
        self.surname=surname
class child(family):
    def __init__(self, surname,name):
        super().__init__(surname)        
        self.name=name
child=child("gowda","ajay")
print(f"{child.name} {child.surname}")        

class user:
    def __init__(self,username):
        self.username=username
    def login(self):
        print(f"{self.username} logged in ")
class admin(user):
    def delete_user(self,user):            
        print(f"admin {self.username} deleted user {user}")
Admin=admin("karnataka_admin")
Admin.login()
Admin.delete_user("user_102")        

class Animals:
    def make_sound(self):
        pass
class cat(Animals):       
    def make_sound(self):
        print("meow")
class dog(Animals):
    def make_sound(self):
        print("bark")        

animals=[dog(),cat()]
for animal in animals:
    print(animal.make_sound())
        
class Notification:
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        print("sending Email")
class SMSNotification(Notification):
    def send(self):
        print("sending sms")
notifications=[EmailNotification(),SMSNotification()]
for notification in notifications:
    notification.send()                

class student:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def get_age(self):
        return self._age
    def set_age(self,age):
        if age>0:
            self._age=age
        else:
            print("invalid age")        
student=student("anita",20)
print("age: ",student.get_age())
student.set_age(21)
print("updated age: ",student.get_age())            
        
class mathoperation:
    def add (self,a,b,c=0):
        return a+b+c
math=mathoperation()
print(math.add(5,10))
print(math.add(5,10,15))


class animal:
    def sound(self):
        print("this animal makes a sound")
class Dog(animal):
    def sound(self):
        print("dog barks")
animals=animal()
animals.sound() 
dog=Dog()
dog.sound()      

class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} makes a sound")
class dog(animal):
    def __init__(self, name,breed):
        super().__init__(name)   
        self.breed=breed
    def sound(self):
        super().sound()
        print(f"{self.name} barks")

Dog=dog("buddy","labrador")
Dog.sound()                     
            
from abc import ABC,abstractmethod  
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class car(vehicle):
    def start_engine(self):
        print("car engine started")

            


                