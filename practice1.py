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