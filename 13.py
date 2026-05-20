#prime numbers check

num=int(input("enter a number: "))

if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number ")
            break
    else:
        print("prime number")
else:
    print("not a prime number")

name =input("enter student name: ")

sub1=int(input("enter marks of subject 1: "))
sub2=int(input("enter marks of subject 2: "))
sub3=int(input("enter marks of subject 3: "))
sub4=int(input("enter marks of subject 4: "))


