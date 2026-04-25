name ="kavana"
age =19
print("My name is",name)
print("My age is",age)
x=10
y=20
print(type(x))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)
numbers=[10,20,30,40,50]
total=0
for num in numbers:
    total=total+num
print(total)    
numbers=[1,2,3,4,5,6]
doubled=[]
for num in numbers:
    doubled.append(num*2)
print("doubled list: ",doubled)
foods=["dosa","idly","vada"]
for food in foods:
    print(f"i like {food}")
student_marks={"anand":85,"geetha":90,"kumar":78}
for student,marks in student_marks.items():
    print(f"{student} scored {marks} marks")    
numbers=[1,2,3,4,5]
squares=[num**2 for num in numbers ]
print(squares)    