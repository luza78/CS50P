import random
import sys


def main():
    # Set difficulty, validating input
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                break
            else:
                pass

    # Pick number
    correct_number = random.randint(1, level)

    # Prompt user for guess, until they pick the correct one
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess > correct_number:
                print("Too large!")
            elif guess < correct_number:
                print("Too small!")
            else:
                sys.exit("Just right!")


main()
