class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"car brand: {self.brand} , model: {self.model}")

my_car=car("toyota","corolla")
my_car.display_info()   

