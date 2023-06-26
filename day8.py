def main():
    print("Welcome to Caesar Cipher")
    print("Press 1 to Encrypt\nPress 2 to Decrypt")
    user_input =int(input())
    if user_input==1:
        encrypt()
    if user_input==2:
        decrypt()
      

def encrypt():
    Ostring = input("Enter the original string: ")
    for i in range(len(Ostring)):
        


def decrypt():
    Estring = input("Enter the Encrypted string: ")
    