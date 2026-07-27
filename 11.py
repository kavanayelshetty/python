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

