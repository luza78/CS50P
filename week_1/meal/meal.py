def main():
    time = input("What time is it? ").strip()
    time = convert(time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")

    elif time >= 12.0 and time <= 13.0:
        print("lunch time")

    elif time >= 18.0 and time <= 19.0:
        print("dinner time")


def convert(time):
    # Split the input into a list by the ":"
    time = time.split(":")
    # Covert to minutes to float, and adds them back together
    time = float(time[0]) + float(time[1]) / 60
    return round(time, 2)


if __name__ == "__main__":
    main()
