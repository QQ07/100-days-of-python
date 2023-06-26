print("Welcome to Tip Calculator")
tot = int(input("What was the total bill? "))
n = int(input("How many people to split the bill "))
tip = int(input("What % tip would you like to give? "))

x = (tot+ (tip/100)*tot)/n
print("Each person should pay ", x, "Rs")