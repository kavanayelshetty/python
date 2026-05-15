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

    
        