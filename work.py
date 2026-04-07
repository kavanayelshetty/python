for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    if i%3==0 or i%5==0:
        print(i,end=" ")
print(" ")
t=20
if t==20:
    print("its time for dinner")
else:
    print("its not a time for dinner")
print(" ")
age=int(input("enter your age: "))
if age>=18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")    