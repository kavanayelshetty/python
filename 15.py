#import time
#for i in range(5,0,-1):
    #print(i)
    #time.sleep(1)

#print("time's up! ")

text=input("enter a word: ")

if text==text[::-1]:
    print("Palindrome")
else:
    print("not a Palindrome")    

sentence=input("Enter a sentence: ")
words=sentence.split()
print("Total words: ",len(words))

num=int(input("enter a number: "))

for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
    else:
        print("prime")