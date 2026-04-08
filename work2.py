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