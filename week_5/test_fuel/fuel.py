def main():
    while True:
        fuel = input("Fraction: ")
        percentage = convert(fuel)
        fuel_status = gauge(percentage)
        if percentage is not None and fuel_status is not None:
            print(f"{fuel_status}")
            break
        else:
            continue


def convert(user_input):
    # 'Try to partition on '/', and 'try' to cast as int, and 'try' to index into partition
    user_input_partitioned = user_input.partition("/")
    if int(user_input_partitioned[2]) == 0:
        raise ZeroDivisionError
    elif int(user_input_partitioned[0]) > int(user_input_partitioned[2]):
        raise ValueError
    fraction = int(user_input_partitioned[0]) / int(user_input_partitioned[2])
    return int(round(fraction * 100))


def gauge(percentage):
    try:
        if percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
    except TypeError:
        return None
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
