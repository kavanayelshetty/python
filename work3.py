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
for i in range(1,6):
    for j in range(1,6):
        print(f"{i} x {j} = {i*j}")
    print()       
cities=["bengaluru","mysure","gulbarga","hubballi"]
for index,city in enumerate(cities):
    print(f"city {index+1} : {city}")

