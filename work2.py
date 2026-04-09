alphabet="apple"
letter=input("letter: ")
def letter_find(name_letter):
    for index,alphabet in enumerate(letter):
        if letter==alphabet:
            print("letter found")
            return index
    print("letter not found")
    return-1
result=letter_find(letter)
print("index:",result)
number_of_values=int(input("enter how many numbers: "))
number_list=[ ]
for i in range(number_of_values):
    number=float(input("enter a number: "))
    number_list.append(number)
mean=sum(number_list)/number_of_values
variance_sum=0
for number in number_list:
    variance_sum+=(number-mean)**2
variance=variance_sum/number_of_values
standard_deviation=variance**0.5
print("mean: ",mean)
print("variance: ",variance)
print("standard deviation: ",standard_deviation)
N=int(input("enter the number of terms "))
first=0
second=1
print("fibnocei sequence: ")
for i in range(N):
    print(first,end=" ")
    next_term=first+second
    first=second
    second=next_term
