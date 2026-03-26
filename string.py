first_name="kavana"
last_name="yelshetty"
print(first_name+" "+last_name)
name="kavana " * 3
print(name )
fruit="apple"
print(" ".join(["apple"]*3))
for i in range(3):
    print("hi",end=" ")
print("done")    
for x in range(4):
        for y in range(1,6):
            print(x,end=" ")
            print(y,end=" ")
            print("")
print("completed")    
prog="python"
print(prog[0:4])     
girl_name=input("girl name: ")
girl_age=int(input("girl age: "))
boy_name=input("boy name: ")  
boy_age=int(input("boy age: "))
age_diff=boy_age - girl_age
print(girl_name + " loves " + boy_name+ " age diff is " + str(age_diff))
your_name=input("your name: ")
age=int(input("your age: "))
if age>=18:
     print("eligible for voting")
else:
     print("not eligible")     