#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 15, 2023
# This program generates a random number from 0-9 and the user must guess it. It uses while true loops and a break statement.

import random

def main():
    # introduce program to user
    print("This program is a guessing game and you must guess the number from 0-9!\n")

    # generate random number
    correct_guess = random.randint(0, 9)

    # do..while loop
    while True:

        # get user guess
        user_guess_str = input("Please guess a number from 0-9: ")

        # try converting user guess to an integer
        try:
            user_guess_int = int(user_guess_str)

            # check if user guess is negative
            if user_guess_int < 0:
                print("{} is not a positive integer.\n".format(user_guess_int))

            # if user guess is positive check if correct guess equals user guess
            elif correct_guess == user_guess_int:
                print("You guessed correctly!\n")
                break
            
            # if user guess is wrong ask them to try again
            else:
                print(
                    "{} is not the correct guess, try again!\n".format(user_guess_int)
                )

        # catching invalid user inputs
        except Exception:
            print("{} is not a positive integer\n".format(user_guess_str))


if __name__ == "__main__":
    main()
