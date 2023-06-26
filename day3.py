print("Welcome to treasure island")
in1 = input("left or right ")
if(in1.lower()!="left"):
    print("Fall into hole. \nGame Over")
    exit()

in2= input("Swim or wait? ")
if(in2.lower()!="wait"):
    print("Attacked by trout.\nGame Over")
    exit()

in3= input("Which door? \n(Red/Blue/Yellow) ")
in3=in3.lower()
if(in3=="Red"):
    print("Burned by fire.\nGame Over")
elif in3=="blue":
    print("Eaten by beasts.\nGame Over")
elif in3=="yellow":
    print("You Win! Congratulations!!")
else:
    print("Game Over!")