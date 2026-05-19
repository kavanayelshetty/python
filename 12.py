#simple calculator

print("----simple calculator----")

num1=float(input("enter firest number: "))
num2=float(input("enter second number: "))

print("\nchoose operation")
print("1. Addition")
print("2.substraction")
print("3.multiplication")
print("4.division")

choice=int(input("enter choice between 1 - 4: "))

if choice==1:
    result=num1+num2
    print("result: ",result)
elif choice==2:
    result=num1-num2
    print("result: ",result) 
elif choice==3:
    result=num1*num2
    print("result: ",result)
elif choice==4:
    if num2!=0:
        result=num1/num2
        print("result: ",result)
    else:
        print("Error! division by zero is not allowed")
else:
    print("invalid input please enter number from 1-4 ")

print("Thank you for using calculator!")            
