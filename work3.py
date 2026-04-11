my_list=[10,20,30,40]
print("initial list:",my_list)
my_list.insert(2,25)
print("after appending 50: ",my_list)
length=len(my_list)
print("length of the list:",length)
popped_element=my_list.pop()
print("popped element:",popped_element)
print("after pooping:",my_list)
my_list.clear()
print("after clearing the list:",my_list)
name=input("enter your name: ")
year_of_birth=int(input("enter your year of birth: "))
current_year=2026
age=current_year-year_of_birth
if age>=60:
    print(name,"is a senior citizen")
else:
    print(name,"is not a senior citizen")    
available_seats=2
while available_seats>0:
    print(f"{available_seats} seats avalaible")
    booking=input("do you want to book a seat?(yes/no):").lower()
if booking=="yes":
        available_seats=1
        print("seat booked!")
else:
        print("no booking made")
print("all seats are booked !")     

