#rock paper scissors

a=input("choose rock/paper/scissor: ")
b=input("choose rock/paper/scissor: ")

if a==b:
    print("draw")
elif(a=="rock" and b=="scissors") or (a=="paper" and b=="rock") or (a=="scissor" and b=="paper"):
    print("player 1 wins")
else:
    print("player 2 wins")        