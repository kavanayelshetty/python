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


        