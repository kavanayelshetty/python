def welcome(func):
    def wrapper():
        print("namaskara")
        func()
        print("take care!")
    return wrapper    