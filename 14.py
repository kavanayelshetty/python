import pandas as pd
s1= pd.Series(12,index=[1,2,3,4,5])
s2=pd.Series(12,index=[1,2,3,4])
print(s1+s2)

list_1=[[1,2,3,4,5],[6,7,8,9,10]]
var1=pd.DataFrame(list_1)
print(var1)

num = 153
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

dict1 = {"name": "Kavana", "age": 19}
dict2 = {"course": "CSE", "year": 2}

result = {**dict1, **dict2}

print(result)    