import random
import sys


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        for j in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            else:
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    # If 3 incorrect answers shows answer
                    if j == 3 - 1:
                        print(f"{x} + {y} = {correct_answer} ")
                    continue

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            # If value between 1-3 includisve
            if 1 <= level <= 3:
                return level
            else:
                pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
