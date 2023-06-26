import random

def prrint(x):
    if x==0:
        print("stone\n")
    elif x==1:
        print("paper\n")
    elif x==2:
        print("scissor\n")
        
c = random.randint(0,2)
h = int(input("0-stone\n1-paper\n2-scissor    "))

print("\nComputer's Move: ")
prrint(c)

print("Your Move: ")
prrint(h)

if c==h:
    print("it's a tie")
elif c+1 == h:
    print("🎉Congratulations!!🥳You won!")
elif h+1 == c:
    print("You lose")
elif h+2 == c:
    print("🎉Congratulations!!🥳You won!")
else: print("You lose!")    
    