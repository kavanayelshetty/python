fruits = ["apple","banana","cherry"]
print(fruits)
print(fruits[1])
fruits[2]="mango"
print(fruits)
fruits.append("grapes")
fruits.insert(2,"kiwi")
print(fruits)
fruits.remove("banana")
print(fruits)
print(len(fruits))
numbers=[1,5,4,7,8,6]
print(numbers)
print(sorted(numbers))
print(sum(numbers))
import string
def remove_punctuation():
    phrase="hi! morning how are you?"
    plain_text=" "
    for letter in phrase:
        if letter not in string.punctuation:
            plain_text=plain_text+letter
    return plain_text
plain_text=remove_punctuation()
print(plain_text)        


