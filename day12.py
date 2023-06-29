'''# Number guessing game'''

import random


def give_me_a_number():
    '''Returns a number which isn't divisible by 5'''
    a_number = int(random.random() * 100)
    while a_number % 5 == 0:  # to make sure that the number isn't divisible by 5
        a_number = int(random.random() * 100)
    return a_number


def start():
    '''Main function'''
    print("Welcome to the Number guessing Game!")
    print("I'm Thinking of a number between 1 and 100")
    final_number = give_me_a_number()
    # print(final_number)
    rem_attempts = 10
    while rem_attempts != 0:
        print(f"You have {rem_attempts} attempts remaining to guess the number: ")
        guessed_number = int(input("Make a guess: "))
        if final_number == guessed_number:
            print("🎉Congratulations!!🎉 You won!!!🥳🥳")
            break
        if guessed_number > final_number:
            print("Lower")
        if guessed_number < final_number:
            print("Higher")
        rem_attempts -= 1
    if final_number!=guessed_number:
        print("😿Sorry! you lost😔")
        print(f"I was thinking of {final_number}")


start()
