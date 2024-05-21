def main():
    fuel = get_fuel("Fraction: ")
    print(f"{fuel}")


def get_fuel(prompt):
    while True:
        # Get str
        user_input = input(prompt)

        try:
            # 'Try to partition on '/', and 'try' to cast as int, and 'try' to index into partition
            user_input_partitioned = user_input.partition("/")
            fraction = int(user_input_partitioned[0]) / int(user_input_partitioned[2])
        except (ValueError, IndexError, ZeroDivisionError):
            # Handles potential errors, reprompting the user until they give valid input
            pass
        else:
            # If X is greater than Y reprompt
            if int(user_input_partitioned[0]) > int(user_input_partitioned[2]):
                continue
            fraction = round(fraction * 100)
            if fraction >= 99:
                return "F"
            elif fraction <= 1:
                return "E"
            else:
                return str(fraction) + "%"


main()
