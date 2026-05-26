# #rock paper scissors

# a=input("choose rock/paper/scissor: ")
# b=input("choose rock/paper/scissor: ")

# if a==b:
#     print("draw")
# elif(a=="rock" and b=="scissors") or (a=="paper" and b=="rock") or (a=="scissor" and b=="paper"):
#     print("player 1 wins")
# else:
#     print("player 2 wins")  /


arr =[5,2,8,1,9]

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print("sorted: ",arr)     

stack=[]

stack.append(10)
stack.append(20)
stack.append(30)

print("popped: ",stack.pop())
print("stack: ",stack)