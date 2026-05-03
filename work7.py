fruits={"apple","banana","cherry"}
print(fruits)
number={1,2,3,4,5}
number2={3,8,9,7,6}
union_set= fruits| number|number2
print(union_set)
set=number-number2
print(set)
set2=number^number2
print(set2)
fruits.remove("banana")
print(fruits)