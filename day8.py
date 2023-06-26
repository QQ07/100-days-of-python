"""encrypt decrypt"""


def main():
    """Main Function"""
    print("Welcome to Caesar Cipher")
    print("Press 1 to Encrypt\nPress 2 to Decrypt")
    user_input = int(input())
    if user_input == 1:
        encrypt()
    if user_input == 2:
        decrypt()


def encrypt():
    """A function that Encrypts"""
    original_string = input("Enter the original string: ")
    ans = ""
    for i in original_string:
        ans += chr(ord(i) + 5)
    print(F"Encrypted String: {ans}")


def decrypt():
    """A function that Decrypts"""
    encrypted_string = input("Enter the Encrypted string: ")
    ans = ""
    for i in encrypted_string:
        ans += chr(ord(i) - 5)
    print(f"Decrypted String: {ans}")


TO_CONTINUE = True
while TO_CONTINUE:
    main()
    u_i = input("Continue? ").lower()
    if u_i == "no":
        TO_CONTINUE = False
