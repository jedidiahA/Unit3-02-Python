#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Dec 8, 2021
# This program checks if users guess is correct.
import constants


def main():
    # get number of students
    number_guessed = int(input("Enter the number:"))
    print("")

    # check if the guess is correct
    if number_guessed == constants.CORRECT:
        print("You guessed correctly")

    # check if the guess is correct
    if number_guessed != constants.CORRECT:
        print("You guessed wrong!")


if __name__ == "__main__":
    main()
