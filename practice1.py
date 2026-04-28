numbers=[1,2,3,4,5,6]
squares=[num**2 for num in numbers]
print(squares)

numbers=[1,2,3,4,5,6,7,8]
even_numbers=[num for num in numbers if num%2==0]
print(even_numbers)

cities=["bengaluru","hubbali","kolar","mysuru"]
uppercase_cities=[city.upper() for city in cities]
print(uppercase_cities)

numbers=[1,2,3,4,5,6]
squares_dict={num:num**2 for num in numbers}
print(squares)

names=["anana","geetha","kumar"]
name_lengths={name:len(name) for name in names}
print(name_lengths)

city_population={
    "bengaluru":84,
    "mysuru":11,
    "hubballi":9,
    "mangaluru":5
}
large_cities={city:population for city,population in city_population.items() if population>10}
print(large_cities)

sentence="i love coding in python"
words=sentence.split()
print(words)

for i in range(1,31):
    for j in range(3,4,2):
        print(f"{i}x{j}={i*j}")
print( )

name="kavana"
for letter in name:
    print(letter)

l1=["dosa","idli","ragi mudde","vada"]
l2=[food.upper() for food in l1]
print(l2)

numbers=[1,2,3,4,5]
squares=[number**2 for number in numbers]
print(squares)

cities=["bangalore","gulbarga","mysuru","hassan"]
def city(list):
    print(len(list))
    for item in list:
        print(item,end=" ")
city(cities)
print()

numbers=[1,2,3,4,5,6,7,8,9,10]
squares=[number**2 for number in numbers]
print(squares)
even=[  number for number in numbers if number%2==0]
print(even)

div3=[num for num in range(1,31) if num%3==0]
print(div3)

k=[1,2,3,4,5,6]
name=["even" if num%2==0 else "odd"  for num in k ]
print(name)
nums=[1,2,3,4,5]
mulpy=[num*10 for num in nums]
print(mulpy)

nums=[1,2,3,4,5]
cubic=[num**3 for num in nums]
print(cubic)
