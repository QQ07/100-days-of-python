# password generator

import random as r

print("Welcome to password generator")
l = int(input("How many letters do you want? "))
n = int(input("How many numbers do you want? "))
s = int(input("How many symbols do you want? "))

pwd = ""
for _ in range(int(l/2)):  # for capital letters
    pwd += chr(r.randint(65,91))
for _ in range(l-int(l/2)):  # for small letters
    pwd += chr(r.randint(97,123))
for _ in range(n):  # for numbers
    pwd += str(r.randint(1,11))
for _ in range(s):  # for symbols
    pwd += chr(r.randint(33,48))

pwd = r.sample(pwd,len(pwd))
pwd = "".join(pwd)
print(f"Here's your password: {pwd}")
